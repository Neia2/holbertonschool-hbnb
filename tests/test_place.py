#!/usr/bin/python3
import unittest
from models.user import User
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user = User(email="host@example.com", name="Host User", password="password")
        self.place = Place(name="Test Place", description="A place to test", latitude=0.0, longitude=0.0, price_per_night=100, max_guests=4, host=self.user)

    def test_place_creation(self):
        self.assertIsInstance(self.place, Place)

    def test_host_assignment(self):
        new_host = User(email="newhost@example.com", name="New Host", password="newpassword")
        with self.assertRaises(Exception):
            self.place.set_host(new_host)

if __name__ == "__main__":
    unittest.main()
