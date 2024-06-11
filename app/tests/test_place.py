#!/usr/bin/python3
"""
Place test
"""

import unittest
from app.models.place import Place
from app.persistence.data_manager import DataManager
import os

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_place_data.json', {})

    def tearDown(self):
        if os.path.exists('test_place_data.json'):
            os.remove('test_place_data.json')

    def test_create_place(self):
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