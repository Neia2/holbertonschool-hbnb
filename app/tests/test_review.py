#!/usr/bin/python3
"""
Review test
"""

import unittest
from app.models.review import Review
from app.persistence.data_manager import DataManager
import os

class TestReview(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_review_data.json', {})

    def tearDown(self):
        if os.path.exists('test_review_data.json'):
            os.remove('test_review_data.json')

    def test_create_review(self):
        review = Review('Babar', 'Maison de Babar', '5', 'Good place' )
        self.data_manager.save(review)
        retrieved_review = self.data_manager.get(review.id, 'review')
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review['rating'], '5')

    def test_update_review(self):
        review = Review('Dink', 'Maison de Dink', '1', 'Bad place' )
        self.data_manager.save(review)
        review.rating = '3'
        self.data_manager.update(review)
        retrieved_review = self.data_manager.get(review.id, 'review')
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review['rating'], '3')

    def test_delete_review(self):
        review = Review('Hulk', 'Maison de Hulk', '4', 'Nice place' )
        self.data_manager.save(review)
        self.data_manager.delete(review.id, 'review')
        retrieved_review = self.data_manager.get(review.id, 'review')
        self.assertIsNone(retrieved_review)

if __name__ == '__main__':
    unittest.main()
