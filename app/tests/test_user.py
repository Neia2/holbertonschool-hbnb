#!/usr/bin/python3
"""
user test
"""

import unittest
from app.models.user import User
from app.persistence.data_manager import DataManager

class TestUser(unittest.TestCase):
    def setUp(self):
        User.email_set.clear()
        self.data_manager = DataManager('test_data.json', {})

    def tearDown(self):
        import os
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_create_user(self):
        user = User('test@example.com', 'Test', 'User')
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user.id, 'user')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], 'test@example.com')

    def test_unique_email(self):
        user1 = User('test@example.com', 'Test', 'User')
        user2 = User('test@example.com', 'Test', 'User2')
        self.data_manager.save(user1)
        with self.assertRaises(Exception):
            self.data_manager.save(user2)

if __name__ == '__main__':
    unittest.main()
