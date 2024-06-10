#!/usr/bin/python3
"""
user test
"""

import unittest
from app.models.city import City
from app.persistence.data_manager import DataManager
import os

class TestCity(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_city_data.json', {})

    def tearDown(self):
        if os.path.exists('test_city_data.json'):
            os.remove('test_city_data.json')

    def test_create_city(self):
        city = City('Paris', 'France')
        self.data_manager.save(city)
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city['name'], 'Paris')
        self.assertEqual(retrieved_city['country_id'], 'France')

    def test_update_city(self):
        city = City('Paris', 'France')
        self.data_manager.save(city)
        city.name = 'Lyon'
        self.data_manager.update(city)
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city['name'], 'Lyon')

    def test_delete_city(self):
        city = City('Paris', 'France')
        self.data_manager.save(city)
        self.data_manager.delete(city.id, 'city')
        retrieved_city = self.data_manager.get(city.id, 'city')
        self.assertIsNone(retrieved_city)


if __name__ == '__main__':
    unittest.main()