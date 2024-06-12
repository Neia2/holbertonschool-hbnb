# tests/test_country_city_endpoints.py
import unittest
from app import app, db
from models.country import Country
from models.city import City

class CountryCityEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

        country_us = Country(code='US', name='United States')
        country_ca = Country(code='CA', name='Canada')
        db.session.add(country_us)
        db.session.add(country_ca)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))
        self.assertGreater(len(data), 0)

    def test_get_country(self):
        response = self.app.get('/countries/US')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['code'], 'US')
        self.assertEqual(data['name'], 'United States')

        response = self.app.get('/countries/XX')
        self.assertEqual(response.status_code, 404)

    def test_get_country_cities(self):
        response = self.app.get('/countries/US/cities')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))

        response = self.app.get('/countries/XX/cities')
        self.assertEqual(response.status_code, 404)

    def test_create_city(self):
        response = self.app.post('/cities', json={
            'name': 'New York',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'New York')
        self.assertEqual(data['country_code'], 'US')

        # Test invalid country code
        response = self.app.post('/cities', json={
            'name': 'Fake City',
            'country_code': 'XX'
        })
        self.assertEqual(response.status_code, 400)

        # Test duplicate city name within the same country
        response = self.app.post('/cities', json={
            'name': 'New York',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 409)

    def test_get_cities(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(isinstance(data, list))

    def test_get_city(self):
        response = self.app.post('/cities', json={
            'name': 'Los Angeles',
            'country_code': 'US'
        })
        city_id = response.get_json()['id']

        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Los Angeles')

        response = self.app.get('/cities/invalid_city_id')
        self.assertEqual(response.status_code, 404)

    def test_update_city(self):
        response = self.app.post('/cities', json={
            'name': 'San Francisco',
            'country_code': 'US'
        })
        city_id = response.get_json()['id']

        response = self.app.put(f'/cities/{city_id}', json={
            'name': 'San Francisco Updated',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'San Francisco Updated')

        # Test updating non-existent city
        response = self.app.put('/cities/non_existent_id', json={
            'name': 'Fake City',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_city(self):
        response = self.app.post('/cities', json={
            'name': 'Seattle',
            'country_code': 'US'
        })
        city_id = response.get_json()['id']

        response = self.app.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)

        # Test deleting non-existent city
        response = self.app.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
