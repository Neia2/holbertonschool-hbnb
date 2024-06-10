#!/usr/bin/python3
"""
User routes
"""

from flask import Flask, Blueprint, request, jsonify
from app.models.user import User
from app.persistence.data_manager import DataManager

app = Flask(__name__)
data_manager = DataManager('data.json')

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if 'email' not in data or 'firs_name' not in data or 'last_name' not in data:
        return jsonify({error: 'Missing required fiels'}), 400

@app.route('/users', methods=['GET'])
def get_users():
    users = data_manager.data.get('user', [])
    return jsonify(users), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, 'user')
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = data_manager.get(user_id, 'user')
    if not user:
        return jsonify({"error": "User not found"}), 404
    user.update(data)
    data_manager.update(user)
    return jsonify(user), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data_manager.get(user_id, 'user')
    if not user:
        return jsonify({"error": "User not found"}), 404
    data_manager.delete(user_id, 'user')
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
