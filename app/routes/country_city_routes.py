#!/usr/bin/python3
"""
Country and City Routes

This module defines routes for managing countries
and cities in a web application using Flask.
It includes endpoints for retrieving countries
and cities, creating, updating, and deleting cities.

It preloads countries based on ISO 3166-1 standard
during initialization.
"""

from flask import Blueprint, request, jsonify
from app.models.country import Country
from app.models.city import City
from app.models.countries_data import COUNTRIES
from app.persistence.data_manager import DataManager
import uuid
from datetime import datetime

# Create a Blueprint for country and city routes
country_city_routes = Blueprint('country_city_routes', __name__)

# Initialize a DataManager instance for data management
data_manager = DataManager()

# Pre-load countries based on ISO 3166-1 standard
for country in COUNTRIES:
    data_manager.save(Country(**country))


@country_city_routes.route('/countries', methods=['GET'])
def get_countries():
    """
    Retrieve a list of all countries.

    Returns:
        JSON: JSON response with a list of all countries.
    """
    countries = data_manager.get_all("Country")
    return jsonify(countries), 200


@country_city_routes.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    """
    Retrieve detailed information about a specific country.

    Args:
        country_code (str): Code of the country to retrieve.

    Returns:
        JSON: JSON response with the country data or an error message if country not found.
    """
    country = next((country for country in data_manager.get_all("Country") if country['code'] == country_code), None)
    if country:
        return jsonify(country), 200
    return jsonify({"error": "Country not found"}), 404


@country_city_routes.route('/countries/<country_code>/cities', methods=['GET'])
def get_country_cities(country_code):
    """
    Retrieve a list of cities for a specific country.

    Args:
        country_code (str): Code of the country for which to retrieve cities.

    Returns:
        JSON: JSON response with a list of cities in the specified country or an error message if country not found.
    """
    country = next((country for country in data_manager.get_all("Country") if country['code'] == country_code), None)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    cities = data_manager.get_all('City')
    country_cities = [city for city in cities if city['country_code'] == country_code]
    return jsonify(country_cities), 200


@country_city_routes.route('/cities', methods=['POST'])
def create_city():
    """
    Create a new city.

    Validates input data and creates a new city object if all validations pass.
    Ensures city name is unique within the same country.
    Responds with the created city data or appropriate error messages.

    Returns:
        JSON: JSON response with the created city data or error messages.
    """
    data = request.get_json()
    is_valid, message = validate_city_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    # Ensure unique city name within the same country
    cities = data_manager.get_all('City')
    if any(city['name'] == data['name'] and city['country_code'] == data['country_code'] for city in cities):
        return jsonify({'error': 'City name already exists in this country'}), 409

    city = City(
        id=str(uuid.uuid4()),
        name=data['name'],
        country_code=data['country_code'],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    data_manager.save(city)
    return jsonify(city.to_dict()), 201


@country_city_routes.route('/cities', methods=['GET'])
def get_cities():
    """
    Retrieve a list of all cities.

    Returns:
        JSON: JSON response with a list of all cities.
    """
    cities = data_manager.get_all('City')
    return jsonify(cities), 200


@country_city_routes.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """
    Retrieve detailed information about a specific city.

    Args:
        city_id (str): ID of the city to retrieve.

    Returns:
        JSON: JSON response with the city data or an error message if city not found.
    """
    city = data_manager.get(city_id, 'City')
    if city:
        return jsonify(city), 200
    return jsonify({'error': 'City not found'}), 404


@country_city_routes.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """
    Update an existing city’s information.

    Args:
        city_id (str): ID of the city to update.

    Returns:
        JSON: JSON response indicating success or failure of the update operation.
    """
    data = request.get_json()
    is_valid, message = validate_city_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400

    city_data = data_manager.get(city_id, 'City')
    if not city_data:
        return jsonify({'error': 'City not found'}), 404

    # Ensure unique city name within the same country
    cities = data_manager.get_all('City')
    if any(city['name'] == data['name'] and city['country_code'] == data['country_code'] and city['id'] != city_id for city in cities):
        return jsonify({'error': 'City name already exists in this country'}), 409

    city = City(
        id=city_id,
        name=data['name'],
        country_code=data['country_code'],
        created_at=city_data['created_at'],
        updated_at=datetime.utcnow()
    )
    data_manager.update(city)
    return jsonify(city.to_dict()), 200


@country_city_routes.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Delete a specific city.

    Args:
        city_id (str): ID of the city to delete.

    Returns:
        JSON: JSON response indicating success or failure of the delete operation.
    """
    city = data_manager.get(city_id, 'City')
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data_manager.delete(city_id, 'City')
    return '', 204


def validate_city_data(data):
    """
    Validate city data.

    Args:
        data (dict): Data representing the city.

    Returns:
        bool: True if data is valid, False otherwise.
        str: Error message if data is invalid.
    """
    if 'name' not in data or not data['name']:
        return False, 'City name is required'
    if 'country_code' not in data or not data['country_code']:
        return False, 'Country code is required'
    if not data_manager.get(data['country_code'], 'Country'):
        return False, 'Invalid country code'
    return True, ''
