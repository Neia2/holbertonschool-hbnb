#!/usr/bin/python3
"""
Unit tests for the City model and its persistence using DataManager.

This module defines a set of unit tests for the City model to ensure
that the basic CRUD (Create, Read, Update, Delete) operations function
correctly with the DataManager class.

Test cases:
- test_create_city: Tests the creation and retrieval of a City.
- test_update_city: Tests the update of a City's name.
- test_delete_city: Tests the deletion of a City.

Classes:
- TestCity: Inherits from unittest.TestCase and provides setup and teardown
  methods to manage test data, along with the test cases.
"""

import unittest
from app.models.city import City
from app.persistence.data_manager import DataManager
import os


class TestCity(unittest.TestCase):
    """
    Test suite for City model using the DataManager for persistence.

    Methods:
    - setUp: Initializes the DataManager with a test data file.
    - tearDown: Cleans up the test data file after each test.
    - test_create_city: Validates creation and retrieval of a City.
    - test_update_city: Validates updating a City's name.
    - test_delete_city: Validates deletion of a City.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes a DataManager instance with a test data
        file named 'test_city_data.json'. This file is used to store
        data for testing purposes.
        """
        self.data_manager = DataManager('test_city_data.json')

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method removes the test data file 'test_city_data.json'
        if it exists, ensuring that each test runs with a clean state.
        """
        if os.path.exists('test_city_data.json'):
            os.remove('test_city_data.json')

    def test_create_city(self):
        """
        Test the creation and retrieval of a City.

        This test creates a new City instance with the name 'Paris'
        and country_id 'France',
        saves it using the DataManager,
        and retrieves it to verify that it was saved correctly.
        """
        city = City('Paris', 'France')
        self.data_manager.save(city)
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city['name'], 'Paris')
        self.assertEqual(retrieved_city['country_id'], 'France')

    def test_update_city(self):
        """
        Test updating a City's name.

        This test creates a new City instance with the name 'Paris'
        and country_id 'France',
        saves it, updates the name to 'Lyon',
        and then retrieves it to verify that the
        update was applied correctly.
        """
        city = City('Paris', 'France')
        self.data_manager.save(city)
        city.name = 'Lyon'
        self.data_manager.update(city)
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city['name'], 'Lyon')

    def test_delete_city(self):
        """
        Test deleting a City.

        This test creates a new City instance with the name 'Paris'
        and country_id 'France',
        saves it, deletes it using the DataManager,
        and attempts to retrieve it to verify
        that it was deleted correctly.
        """
        city = City('Paris', 'France')
        self.data_manager.save(city)
        self.data_manager.delete(city.id, 'city')
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertIsNone(retrieved_city)


if __name__ == '__main__':
    unittest.main()
