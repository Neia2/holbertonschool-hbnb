#!/usr/bin/python3
"""
country test
"""

import unittest
from app.models.country import Country
from app.persistence.data_manager import DataManager
import os

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_country_data.json', {})

    def tearDown(self):
        if os.path.exists('test_country_data.json'):
            os.remove('test_country_data.json')
    
    def test_create_country(self):
        country = Country('France', '74500')
        self.data_manager.save(country)
        retrieved_country = self.data_manager.get(country.id, 'country')
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country['name'], 'France')
        self.assertEqual(retrieved_country['code'], '74500')

    def test_update_country(self):
        country = Country('France', '74500')
        self.data_manager.save(country)
        country.name = 'Italie'
        self.data_manager.update(country)
        retrieved_country = self.data_manager.get(country.id, 'country')
        self.assertIsNotNone(retrieved_country)
        self.assertEqual(retrieved_country['name'], 'Italie')

    def test_delete_country(self):
        country = Country('France', '74500')
        self.data_manager.save(country)
        self.data_manager.delete(country.id, 'country')
        retrieved_country = self.data_manager.get(country.id, 'country')
        self.assertIsNone(retrieved_country)

if __name__ == '__main__':
    unittest.main()