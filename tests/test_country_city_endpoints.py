import unittest
from flask import Flask
from api.country_city_routes import country_city_routes

class CountryCityEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(country_city_routes)
        self.client = self.app.test_client()

    def test_get_countries(self):
        response = self.client.get('/countries')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))
        self.assertGreater(len(data), 0)

    def test_get_country(self):
        response = self.client.get('/countries/US')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['code'], 'US')
        self.assertEqual(data['name'], 'United States')

        response = self.client.get('/countries/XX')
        self.assertEqual(response.status_code, 404)

    def test_get_country_cities(self):
        response = self.client.get('/countries/US/cities')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))

        response = self.client.get('/countries/XX/cities')
        self.assertEqual(response.status_code, 404)

    def test_create_city(self):
        response = self.client.post('/cities', json={
            'name': 'New York',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'New York')
        self.assertEqual(data['country_code'], 'US')

        # Test invalid country code
        response = self.client.post('/cities', json={
            'name': 'Fake City',
            'country_code': 'XX'
        })
        self.assertEqual(response.status_code, 400)

        # Test duplicate city name within the same country
        response = self.client.post('/cities', json={
            'name': 'New York',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 409)

    def test_get_cities(self):
        response = self.client.get('/cities')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))

    def test_get_city(self):
        response = self.client.post('/cities', json={
            'name': 'Los Angeles',
            'country_code': 'US'
        })
        city_id = response.get_json()['id']

        response = self.client.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Los Angeles')

        response = self.client.get('/cities/invalid_city_id')
        self.assertEqual(response.status_code, 404)

    def test_update_city(self):
        response = self.client.post('/cities', json={
            'name': 'San Francisco',
            'country_code': 'US'
        })
        city_id = response.get_json()['id']

        response = self.client.put(f'/cities/{city_id}', json={
            'name': 'San Francisco Updated',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'San Francisco Updated')

        # Test updating non-existent city
        response = self.client.put('/cities/non_existent_id', json={
            'name': 'Fake City',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_city(self):
        response = self.client.post('/cities', json={
            'name': 'Seattle',
            'country_code': 'US'
        })
        city_id = response.get_json()['id']

        response = self.client.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)

        # Test deleting non-existent city
        response = self.client.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
