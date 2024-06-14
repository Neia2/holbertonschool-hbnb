# api/country_city_routes.py

from flask_restx import Namespace, Resource
from models.country import Country
from models.city import City

country_ns = Namespace('countries', description='Country operations')
city_ns = Namespace('cities', description='City operations')

@country_ns.route('/')
class CountryList(Resource):
    def get(self):
        return {'message': 'List of countries'}

@city_ns.route('/')
class CityList(Resource):
    def get(self):
        return {'message': 'List of cities'}
