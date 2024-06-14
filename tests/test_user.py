#!/usr/bin/python3

# test_user.py
import unittest
from models import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(email="test@example.com", password="password")

    def test_user_creation(self):
        self.assertIsNotNone(self.user)

    def test_email_unique(self):
        user2 = User(email="test@example.com", password="password")
        self.assertNotEqual(self.user.id, user2.id)

if __name__ == '__main__':
    unittest.main()
