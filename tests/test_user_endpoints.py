#!/usr/bin/python3

# test_user_endpoints.py
import unittest
from app import app
from data_manager import DataManager

class UserEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password'
        })
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password'
        })
        response = self.client.put('/users/1', json={
            'email': 'newtest@example.com',
            'name': 'New Test User'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password'
        })
        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
