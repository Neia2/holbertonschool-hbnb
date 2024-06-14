#!/usr/bin/python3
# test_data_manager.py
import unittest
from data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_user(self):
        user_data = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        self.data_manager.save_user(user_data)
        saved_user = self.data_manager.get_user(1)
        self.assertEqual(saved_user, user_data)

    def test_update_user(self):
        user_data = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        self.data_manager.save_user(user_data)
        updated_data = {'id': 1, 'name': 'John Smith', 'email': 'john.smith@example.com'}
        self.data_manager.update_user(1, updated_data)
        updated_user = self.data_manager.get_user(1)
        self.assertEqual(updated_user, updated_data)

    def test_delete_user(self):
        user_data = {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        self.data_manager.save_user(user_data)
        self.data_manager.delete_user(1)
        deleted_user = self.data_manager.get_user(1)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
