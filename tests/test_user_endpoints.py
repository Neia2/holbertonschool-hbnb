#!/usr/bin/python3
import unittest
from flask import Flask
from api.user_routes import user_routes

class UserEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_routes)
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = response.get_json()['id']
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = response.get_json()['id']
        response = self.client.put(f'/users/{user_id}', json={
            'email': 'updated@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        user_id = response.get_json()['id']
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
