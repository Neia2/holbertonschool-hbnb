#!/usr/bin/python3
import unittest
from models.user import User
from persistence.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_data.json')
        self.user = User(email="test@example.com", name="Test User", password="password")
        self.data_manager.save(self.user)

    def tearDown(self):
        import os
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_save_user(self):
        self.data_manager.save(self.user)
        saved_user = self.data_manager.get(self.user.id, 'User')
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user['email'], "test@example.com")

    def test_update_user(self):
        self.user.name = "Updated User"
        self.data_manager.update(self.user)
        updated_user = self.data_manager.get(self.user.id, 'User')
        self.assertEqual(updated_user['name'], "Updated User")

    def test_delete_user(self):
        self.data_manager.delete(self.user.id, 'User')
        deleted_user = self.data_manager.get(self.user.id, 'User')
        self.assertIsNone(deleted_user)

if __name__ == "__main__":
    unittest.main()
