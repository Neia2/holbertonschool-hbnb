#!/usr/bin/python3
"""
Amenity test
"""

import unittest
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager
import os

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_amenity_data.json', {})

    def tearDown(self):
        if os.path.exists('test_amenity_data.json'):
            os.remove('test_amenity_data.json')

    def test_create_amenity(self):
        amenity = Amenity('Wi-Fi')
        self.data_manager.save(amenity)
        retrieved_amenity = self.data_manager.get(amenity.id, 'amenity')
        self.assertIsNotNone(retrieved_amenity)
        self.assertEqual(retrieved_amenity['name'], 'Wi-Fi')

    def test_update_amenity(self):
        amenity = Amenity('Wi-Fi')
        self.data_manager.save(amenity)
        amenity.name = 'Parking'
        self.data_manager.update(amenity)
        retrieved_amenity = self.data_manager.get(amenity.id, 'amenity')
        self.assertIsNotNone(retrieved_amenity)
        self.assertEqual(retrieved_amenity['name'], 'Parking')

    def test_delete_amenity(self):
        amenity = Amenity('Wi-Fi')
        self.data_manager.save(amenity)
        self.data_manager.delete(amenity.id, 'amenity')
        retrieved_amenity = self.data_manager.get(amenity.id, 'amenity')
        self.assertIsNone(retrieved_amenity)

if __name__ == '__main__':
    unittest.main()
