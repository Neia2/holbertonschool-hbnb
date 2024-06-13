from flask import Blueprint, request, jsonify
from models.user import User
from persistence.data_manager import DataManager
import re

user_routes = Blueprint('user_routes', __name__)
data_manager = DataManager()

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_user_data(data):
    if 'email' not in data or not validate_email(data['email']):
        return False, "Invalid or missing email"
    if 'full_name' not in data or not data['full_name']:
        return False, "Full name is required"
    if 'password' not in data or not data['password']:
        return False, "Password is required"
    return True, ""

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    if data_manager.get(data['email'], 'User'):
        return jsonify({'error': 'Email already exists'}), 409

    user = User(email=data['email'], full_name=data['full_name'], password=data['password'])
    data_manager.save(user)
    return jsonify(user.__dict__), 201

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all('User')
    return jsonify(users), 200

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

    user_data = data_manager.get(user_id, 'User')
    if not user_data:
        return jsonify({'error': 'User not found'}), 404

    user = User(**user_data)
    user.update(email=data['email'], full_name=data['full_name'], password=data['password'])
    data_manager.update(user)
    return jsonify(user.__dict__), 200

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get(user_id, 'User')
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data_manager.delete(user_id, 'User')
    return '', 204
