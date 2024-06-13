#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from app.models.user import User
from app.persistence.data_manager import DataManager
import re

user_routes = Blueprint('user_routes', __name__)
data_manager = DataManager()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_user_data(data):
    if 'email' not in data or not validate_email(data['email']):
        return False, "Invalid or missing email"
    if 'first_name' not in data or not data['first_name']:
        return False, "First name is required"
    if 'last_name' not in data or not data['last_name']:
        return False, "Last name is required"
    return True, ""

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    if data_manager.get(data['email'], 'User'):
        return jsonify({'error': 'Email already exists'}), 409

    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
    data_manager.save(user)
    return jsonify(user.to_dict()), 201

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all('User')
    return jsonify([user for user in users]), 200

@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, 'User')
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    user = data_manager.get(user_id, 'User')
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.update(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
    data_manager.update(user)
    return jsonify(user.to_dict()), 200

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get(user_id, 'User')
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data_manager.delete(user_id, 'User')
    return '', 204