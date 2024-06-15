#!/usr/bin/python3
"""
Unit tests for the Review model and its persistence using DataManager.

This module defines a set of unit tests for the Review model to ensure
that the basic CRUD (Create, Read, Update, Delete) operations function
correctly with the DataManager class.

Test cases:
- test_create_review: Tests the creation and retrieval of a Review.
- test_update_review: Tests the update of a Review's details.
- test_delete_review: Tests the deletion of a Review.

Classes:
- TestReview: Inherits from unittest.TestCase and provides setup and teardown
  methods to manage test data, along with the test cases.
"""

import unittest
from app.models.review import Review
from app.persistence.data_manager import DataManager
import os


class TestReview(unittest.TestCase):
    """
    Test suite for Review model using the DataManager for persistence.

    Methods:
    - setUp: Initializes the DataManager with a test data file.
    - tearDown: Cleans up the test data file after each test.
    - test_create_review: Validates creation and retrieval of a Review.
    - test_update_review: Validates updating a Review's details.
    - test_delete_review: Validates deletion of a Review.
    """

    def setUp(self):
        """
        Set up the test environment before each test.

        This method initializes a DataManager instance with a test data
        file named 'test_review_data.json'. This file is used to store
        data for testing purposes.
        """
        self.data_manager = DataManager('test_review_data.json')

    def tearDown(self):
        """
        Clean up the test environment after each test.

        This method removes the test data file 'test_review_data.json'
        if it exists, ensuring that each test runs with a clean state.
        """
        if os.path.exists('test_review_data.json'):
            os.remove('test_review_data.json')

    def test_create_review(self):
        """
        Test the creation and retrieval of a Review.

        This test creates a new Review instance with specific details,
        saves it using the DataManager, and retrieves it to verify
        that it was saved correctly.
        """
        review = Review('Babar', 'Maison de Babar', '5', 'Good place')
        self.data_manager.save(review)
        retrieved_review = self.data_manager.get(review.id, 'review')
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review['rating'], '5')

    def test_update_review(self):
        """
        Test updating a Review's details.

        This test creates a new Review instance with specific details,
        saves it, updates the rating, and then retrieves it to verify
        that the updates were applied correctly.
        """
        review = Review('Dink', 'Maison de Dink', '1', 'Bad place')
        self.data_manager.save(review)
        review.rating = '3'
        self.data_manager.update(review)
        retrieved_review = self.data_manager.get(review.id, 'review')
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review['rating'], '3')

    def test_delete_review(self):
        """
        Test deleting a Review.

        This test creates a new Review instance with specific details,
        saves it, deletes it using the DataManager, and attempts to
        retrieve it to verify that it was deleted correctly.
        """
        review = Review('Hulk', 'Maison de Hulk', '4', 'Nice place')
        self.data_manager.save(review)
        self.data_manager.delete(review.id, 'review')
        retrieved_review = self.data_manager.get(review.id, 'review')
        self.assertIsNone(retrieved_review)


if __name__ == '__main__':
    unittest.main()
