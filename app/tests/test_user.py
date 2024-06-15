#!/usr/bin/python3
"""
Unit tests for the User model and its persistence using DataManager.

This module defines a set of unit tests for the User model to ensure
that the basic CRUD (Create, Read, Update, Delete) operations function
correctly with the DataManager class. It also tests the uniqueness
constraint on user emails.

Test cases:
- test_create_user: Tests the creation and retrieval of a User.
- test_unique_email: Tests the uniqueness constraint on user emails.

Classes:
- TestUser: Inherits from unittest.TestCase and provides setup and teardown
  methods to manage test data, along with the test cases.
"""

import unittest
from app.models.user import User
from app.persistence.data_manager import DataManager
import os


class TestUser(unittest.TestCase):
    """
    Test suite for User model using the DataManager for persistence.

    Methods:
    - setUp: Initializes the DataManager with a test data file and clears
      any existing email set.
    - tearDown: Cleans up the test data file after each test.
    - test_create_user: Validates creation and retrieval of a User.
    - test_unique_email: Validates uniqueness constraint on user emails.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes a DataManager instance with a test data
        file named 'test_data.json' and clears any existing entries in
        the User.email_set to ensure a clean state for each test.
        """
        User.email_set.clear()
        self.data_manager = DataManager('test_data.json')

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method removes the test data file 'test_data.json'
        if it exists, ensuring that each test runs with a clean state.
        """
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_create_user(self):
        """
        Test the creation and retrieval of a User.

        This test creates a new User instance with specific details,
        saves it using the DataManager, and retrieves it to verify
        that it was saved correctly.
        """
        user = User('test@example.com', 'Test', 'User')
        self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user.id, 'user')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], 'test@example.com')

    def test_unique_email(self):
        """
        Test the uniqueness constraint on user emails.

        This test creates two User instances with the same email, saves
        the first one successfully, and then tries to save the second
        one, expecting an Exception to be raised due to the email already
        existing in User.email_set.
        """
        user1 = User('test1@example.com', 'Test1', 'User1')
        user2 = User('test2@example.com', 'Test2', 'User2')
        self.data_manager.save(user1)
        with self.assertRaises(Exception):
            # Email already exists
            user3 = User('test1@example.com', 'Test1', 'User1')
            self.data_manager.save(user3)


if __name__ == '__main__':
    unittest.main()
