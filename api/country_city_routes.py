# api/country_city_routes.py
from flask_restx import Namespace, Resource
from flask import request
from models.country import Country
from models.city import City
from models.countries_data import COUNTRIES
from persistence.data_manager import DataManager
import uuid
from datetime import datetime

country_ns = Namespace('countries', description='Country related operations')
city_ns = Namespace('cities', description='City related operations')

data_manager = DataManager()

# Pre-load countries on ISO 3166-1 standard
for country in COUNTRIES:
    data_manager.save(Country(**country))

@country_ns.route('/')
class CountryList(Resource):
    def get(self):
        countries = data_manager.get_all("Country")
        return countries, 200

@country_ns.route('/<string:country_code>')
class CountryDetail(Resource):
    def get(self, country_code):
        country = next((country for country in data_manager.get_all("Country") if country['code'] == country_code), None)
        if country:
            return country, 200
        return {"error": "Country not found"}, 404

@country_ns.route('/<string:country_code>/cities')
class CountryCities(Resource):
    def get(self, country_code):
        country = next((country for country in data_manager.get_all("Country") if country['code'] == country_code), None)
        if not country:
            return {'error': 'Country not found'}, 404
        cities = data_manager.get_all('City')
        country_cities = [city for city in cities if city['country_code'] == country_code]
        return country_cities, 200

@city_ns.route('/')
class CityList(Resource):
    def post(self):
        data = request.get_json()
        is_valid, message = validate_city_data(data)
        if not is_valid:
            return {'error': message}, 400

        # Ensure unique city name within the same country
        cities = data_manager.get_all('City')
        if any(city['name'] == data['name'] and city['country_code'] == data['country_code'] for city in cities):
            return {'error': 'City name already exists in this country'}, 409

        city = City(
            id=str(uuid.uuid4()),
            name=data['name'],
            country_code=data['country_code'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        data_manager.save(city)
        return city.to_dict(), 201

    def get(self):
        cities = data_manager.get_all('City')
        return cities, 200

@city_ns.route('/<string:city_id>')
class CityDetail(Resource):
    def get(self, city_id):
        city = data_manager.get(city_id, 'City')
        if city:
            return city, 200
        return {'error': 'City not found'}, 404

    def put(self, city_id):
        data = request.get_json()
        is_valid, message = validate_city_data(data)
        if not is_valid:
            return {'error': message}, 400

        city_data = data_manager.get(city_id, 'City')
        if not city_data:
            return {'error': 'City not found'}, 404

        # Ensure unique city name within the same country
        cities = data_manager.get_all('City')
        if any(city['name'] == data['name'] and city['country_code'] == data['country_code'] and city['id'] != city_id for city in cities):
            return {'error': 'City name already exists in this country'}, 409

        city = City(
            id=city_id,
            name=data['name'],
            country_code=data['country_code'],
            created_at=city_data['created_at'],
            updated_at=datetime.utcnow()
        )
        data_manager.update(city)
        return city.to_dict(), 200

    def delete(self, city_id):
        city = data_manager.get(city_id, 'City')
        if not city:
            return {'error': 'City not found'}, 404

        data_manager.delete(city_id, 'City')
        return '', 204

def validate_city_data(data):
    if 'name' not in data or not data['name']:
        return False, 'City name is required'
    if 'country_code' not in data or not data['country_code']:
        return False, 'Country code is required'
    if not data_manager.get(data['country_code'], 'Country'):
        return False, 'Invalid country code'
    return True, ''
