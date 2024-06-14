import unittest
from flask import Flask
from flask.testing import FlaskClient

# Import your Flask application using correct relative import
from holbertonschool-hbnb.api.app import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        """Tear down test client"""
        pass

    def test_index(self):
        """Test index route"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Country and City API', response.data)

if __name__ == '__main__':
    unittest.main()

