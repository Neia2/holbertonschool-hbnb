#!/usr/bin/python3
"""
Unit tests for the Country model and its persistence using DataManager.

This module defines a set of unit tests for the Country model to ensure
that the basic CRUD (Create, Read, Update, Delete) operations function
correctly with the DataManager class.

Test cases:
- test_create_country: Tests the creation and retrieval of a Country.
- test_update_country: Tests the update of a Country's name.
- test_delete_country: Tests the deletion of a Country.

Classes:
- TestCountry: Inherits from unittest.TestCase and provides setup and teardown
  methods to manage test data, along with the test cases.
"""

import unittest
from app.models.country import Country
from app.persistence.data_manager import DataManager
import os


class TestCountry(unittest.TestCase):
    """
    Test suite for Country model using the DataManager for persistence.

    Methods:
    - setUp: Initializes the DataManager with a test data file.
    - tearDown: Cleans up the test data file after each test.
    - test_create_country: Validates creation and retrieval of a Country.
    - test_update_country: Validates updating a Country's name.
    - test_delete_country: Validates deletion of a Country.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes a DataManager instance with a test data
        file named 'test_country_data.json'. This file is used to store
        data for testing purposes.
        """
        self.data_manager = DataManager('test_country_data.json')

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method removes the test data file 'test_country_data.json'
        if it exists, ensuring that each test runs with a clean state.
        """
        if os.path.exists('test_country_data.json'):
            os.remove('test_country_data.json')

    def test_create_country(self):
        """
        Test the creation and retrieval of a Country.

        This test creates a new Country instance
        with the name 'France' and code '74500',
        saves it using the DataManager,
        and retrieves it to verify that it was saved correctly.
        """
        country = Country('France', '74500')
        self.data_manager.save(country)
        retrieved_country = self.data_manager.get(country.id, 'country')
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country['name'], 'France')
        self.assertEqual(retrieved_country['code'], '74500')

    def test_update_country(self):
        """
        Test updating a Country's name.

        This test creates a new Country instance
        with the name 'France' and code '74500',
        saves it, updates the name to 'Italie',
        and then retrieves it to verify that the
        update was applied correctly.
        """
        country = Country('France', '74500')
        self.data_manager.save(country)
        country.name = 'Italie'
        self.data_manager.update(country)
        retrieved_country = self.data_manager.get(country.id, 'country')
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country['name'], 'Italie')

    def test_delete_country(self):
        """
        Test deleting a Country.

        This test creates a new Country instance
        with the name 'France' and code '74500',
        saves it, deletes it using the DataManager,
        and attempts to retrieve it to verify
        that it was deleted correctly.
        """
        country = Country('France', '74500')
        self.data_manager.save(country)
        self.data_manager.delete(country.id, 'country')
        retrieved_country = self.data_manager.get(country.id, 'country')
        self.assertIsNone(retrieved_country)


if __name__ == '__main__':
    unittest.main()
