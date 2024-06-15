#!/usr/bin/python3
"""
Unit tests for the Place model and its persistence using DataManager.

This module defines a set of unit tests for the Place model to ensure
that the basic CRUD (Create, Read, Update, Delete) operations function
correctly with the DataManager class.

Test cases:
- test_create_place: Tests the creation and retrieval of a Place.
- test_update_place: Tests the update of a Place's details.
- test_delete_place: Tests the deletion of a Place.

Classes:
- TestPlace: Inherits from unittest.TestCase and provides setup and teardown
  methods to manage test data, along with the test cases.
"""

import unittest
from app.models.place import Place
from app.persistence.data_manager import DataManager
import os


class TestPlace(unittest.TestCase):
    """
    Test suite for Place model using the DataManager for persistence.

    Methods:
    - setUp: Initializes the DataManager with a test data file.
    - tearDown: Cleans up the test data file after each test.
    - test_create_place: Validates creation and retrieval of a Place.
    - test_update_place: Validates updating a Place's details.
    - test_delete_place: Validates deletion of a Place.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes a DataManager instance with a test data
        file named 'test_place_data.json'. This file is used to store
        data for testing purposes.
        """
        self.data_manager = DataManager('test_place_data.json')

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method removes the test data file 'test_place_data.json'
        if it exists, ensuring that each test runs with a clean state.
        """
        if os.path.exists('test_place_data.json'):
            os.remove('test_place_data.json')

    def test_create_place(self):
        """
        Test the creation and retrieval of a Place.

        This test creates a new Place instance with specific details,
        saves it using the DataManager, and retrieves it to verify
        that it was saved correctly.
        """
        place = Place(
            name='Lovely Apartment',
            description='A lovely apartment in the city center.',
            address='123 Main St, Cityville',
            city_id='city_123',
            latitude=37.7749,
            longitude=-122.4194,
            host_id='host_123',
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=100,
            max_guest=4
        )
        self.data_manager.save(place)
        retrieved_place = self.data_manager.get(place.id, 'place')
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place['name'], 'Lovely Apartment')
        self.assertEqual(retrieved_place['max_guests'], 4)

    def test_update_place(self):
        """
        Test updating a Place's details.

        This test creates a new Place instance with specific details,
        saves it, updates the name and price per night, and then retrieves
        it to verify that the updates were applied correctly.
        """
        place = Place(
            name='Lovely Apartment',
            description='A lovely apartment in the city center.',
            address='123 Main St, Cityville',
            city_id='city_123',
            latitude=37.7749,
            longitude=-122.4194,
            host_id='host_123',
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=100,
            max_guest=4
        )
        self.data_manager.save(place)
        place.name = 'Updated Apartment'
        place.price_per_night = 120
        self.data_manager.update(place)
        retrieved_place = self.data_manager.get(place.id, 'place')
        self.assertIsNotNone(retrieved_place)
        self.assertEqual(retrieved_place['name'], 'Updated Apartment')
        self.assertEqual(retrieved_place['price_per_night'], 120)

    def test_delete_place(self):
        """
        Test deleting a Place.

        This test creates a new Place instance with specific details,
        saves it, deletes it using the DataManager, and attempts to
        retrieve it to verify that it was deleted correctly.
        """
        place = Place(
            name='Lovely Apartment',
            description='A lovely apartment in the city center.',
            address='123 Main St, Cityville',
            city_id='city_123',
            latitude=37.7749,
            longitude=-122.4194,
            host_id='host_123',
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=100,
            max_guest=4
        )
        self.data_manager.save(place)
        self.data_manager.delete(place.id, 'place')
        retrieved_place = self.data_manager.get(place.id, 'place')
        self.assertIsNone(retrieved_place)


if __name__ == '__main__':
    unittest.main()
