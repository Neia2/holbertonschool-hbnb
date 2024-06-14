# user_routes.py
import re
from flask import request, jsonify
from app import app, db
from models import User
from data_manager import DataManager

data_manager = DataManager('data.json')

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_user_data(data):
    if 'email' not in data or not validate_email(data['email']):
        return False, "Invalid email"
    if 'password' not in data:
        return False, "Password is required"
    return True, ""

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    user = User(email=data['email'], password=data['password'], name=data.get('name'))
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = data_manager.get_all('User')
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get('User', user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = data_manager.get('User', user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    is_valid, message = validate_user_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    user.update(data)
    db.session.commit()
    return jsonify({'id': user.id}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get('User', user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return '', 204
