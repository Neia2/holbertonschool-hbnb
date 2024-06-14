#!/usr/bin/python3
# test_country_city_endpoints.py
import unittest
from app import app, db

class TestCountryCityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)

    def test_get_cities(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

