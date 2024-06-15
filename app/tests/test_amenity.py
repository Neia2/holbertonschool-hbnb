#!/usr/bin/python3
"""
Unit tests for the Amenity model and its persistence using DataManager.

This module defines a set of unit tests for the Amenity model to ensure
that the basic CRUD (Create, Read, Update, Delete) operations function
correctly with the DataManager class.

Test cases:
- test_create_amenity: Tests the creation and retrieval of an Amenity.
- test_update_amenity: Tests the update of an Amenity's name.
- test_delete_amenity: Tests the deletion of an Amenity.

Classes:
- TestAmenity: Inherits from unittest.TestCase and provides setup and teardown
  methods to manage test data, along with the test cases.
"""

import unittest
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager
import os


class TestAmenity(unittest.TestCase):
    """
    Test suite for Amenity model using the DataManager for persistence.

    Methods:
    - setUp: Initializes the DataManager with a test data file.
    - tearDown: Cleans up the test data file after each test.
    - test_create_amenity: Validates creation and retrieval of an Amenity.
    - test_update_amenity: Validates updating an Amenity's name.
    - test_delete_amenity: Validates deletion of an Amenity.
    """
    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes a DataManager instance with a test data
        file named 'test_amenity_data.json'. This file is used to store
        data for testing purposes.
        """
        self.data_manager = DataManager('test_amenity_data.json')

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method removes the test data file 'test_amenity_data.json'
        if it exists, ensuring that each test runs with a clean state.
        """
        if os.path.exists('test_amenity_data.json'):
            os.remove('test_amenity_data.json')

    def test_create_amenity(self):
        """
        Test the creation and retrieval of an Amenity.

        This test creates a new Amenity instance with the name 'Wi-Fi', saves
        it using the DataManager, and retrieves it to verify that it was saved
        correctly.
        """
        amenity = Amenity('Wi-Fi')
        self.data_manager.save(amenity)
        retrieved_amenity = self.data_manager.get(amenity.id, 'amenity')
        self.assertIsNotNone(retrieved_amenity)
        self.assertEqual(retrieved_amenity['name'], 'Wi-Fi')

    def test_update_amenity(self):
        """
        Test updating an Amenity's name.

        This test creates a new Amenity instance with the name 'Wi-Fi', saves
        it, updates the name to 'Parking', and then retrieves it to verify
        that the update was applied correctly.
        """
        amenity = Amenity('Wi-Fi')
        self.data_manager.save(amenity)
        amenity.name = 'Parking'
        self.data_manager.update(amenity)
        retrieved_amenity = self.data_manager.get(amenity.id, 'amenity')
        self.assertIsNotNone(retrieved_amenity)
        self.assertEqual(retrieved_amenity['name'], 'Parking')

    def test_delete_amenity(self):
        """
        Test deleting an Amenity.

        This test creates a new Amenity instance with the name 'Wi-Fi', saves
        it, deletes it using the DataManager, and attempts to retrieve it to
        verify that it was deleted correctly.
        """
        amenity = Amenity('Wi-Fi')
        self.data_manager.save(amenity)
        self.data_manager.delete(amenity.id, 'amenity')
        retrieved_amenity = self.data_manager.get(amenity.id, 'amenity')
        self.assertIsNone(retrieved_amenity)


if __name__ == '__main__':
    unittest.main()
