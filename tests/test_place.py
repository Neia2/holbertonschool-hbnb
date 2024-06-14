#!/usr/bin/python3

# test_place.py
import unittest
from models.user import User
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user = User(email="host@example.com", password="password")

    def test_place_creation(self):
        place = Place(name="Sample Place", user_id=self.user.id)
        self.assertIsNotNone(place)

    def test_host_assignment(self):
        place = Place(name="Sample Place", user_id=self.user.id)
        self.assertEqual(place.user_id, self.user.id)

if __name__ == '__main__':
    unittest.main()
