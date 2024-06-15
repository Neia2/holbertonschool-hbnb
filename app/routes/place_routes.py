#!/usr/bin/python3
"""
Place Routes

This module defines routes for managing places in a web application using Flask.
It includes endpoints for creating, retrieving, updating, and deleting places.
"""

from flask import Blueprint, request, jsonify
from app.models.place import Place
from app.models.amenity import Amenity
from app.persistence.data_manager import DataManager

# Create a Blueprint for place routes
place_routes = Blueprint('place_routes', __name__)

# Initialize a DataManager instance for data management
data_manager = DataManager()


@place_routes.route('/places', methods=['POST'])
def create_place():
    """
    Create a new place.

    Validates input data and creates a new place object if all validations pass.
    Responds with the created place data or appropriate error messages.

    Returns:
        JSON: JSON response with the created place data or error messages.
    """
    data = request.json
    
    # Validate geographical coordinates
    if not (-90 <= data.get('latitude', 0) <= 90) or not (-180 <= data.get('longitude', 0) <= 180):
        return jsonify({'message': 'Invalid geographical coordinates'}), 400
    
    # Validate number of rooms, bathrooms, and max guests
    if not all(isinstance(data.get(field, 0), int) and data.get(field, 0) >= 0 for field in ['num_rooms', 'num_bathrooms', 'max_guests']):
        return jsonify({'message': 'Number of rooms, bathrooms, and max guests must be non-negative integers'}), 400
    
    # Validate price per night
    if not isinstance(data.get('price_per_night', 0), (int, float)) or data.get('price_per_night', 0) < 0:
        return jsonify({'message': 'Price per night must be a valid non-negative numerical value'}), 400
    
    # Validate city_id exists
    city_id = data.get('city_id')
    city = data_manager.get(city_id, 'city')
    if not city:
        return jsonify({'message': 'Invalid city_id. City does not exist'}), 400

    # Validate all amenity_ids exist
    if 'amenity_ids' in data:
        invalid_amenities = [amenity_id for amenity_id in data['amenity_ids'] if not Amenity.query.filter_by(id=amenity_id).first()]
        if invalid_amenities:
            return jsonify({'message': f'Amenities with IDs {invalid_amenities} do not exist'}), 400
    
    # Create a new place if all validations pass
    place = Place(name=data['name'], description=data['description'], address=data['address'], 
                  city_id=data['city_id'], host_id=data['host_id'], latitude=data['latitude'],
                  longitude=data['longitude'], num_rooms=data['num_rooms'], num_bathrooms=data['num_bathrooms'],
                  price_per_night=data['price_per_night'], max_guests=data['max_guests'])
    data_manager.save(place)
    return jsonify(place.to_dict()), 201

@place_routes.route('/places', methods=['GET'])
def get_all_places():
    """
    Retrieve a list of all places.

    Returns:
        JSON: JSON response with a list of all places.
    """
    all_places = data_manager.get_all('place')
    return jsonify(all_places), 200


@place_routes.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """
    Retrieve detailed information about a specific place.

    Args:
        place_id (str): ID of the place to retrieve.

    Returns:
        JSON: JSON response with the place data
        or an error message if place not found.
    """
    place = data_manager.get(place_id, 'place')
    if place:
        return jsonify(place), 200
    else:
        return jsonify({'message': 'Place not found'}), 404


@place_routes.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """
    Update an existing place’s information.

    Args:
        place_id (str): ID of the place to update.

    Returns:
        JSON: JSON response indicating success
        or failure of the update operation.
    """
    data = request.json
    place = data_manager.get(place_id, 'place')
    if place:
        updated_place = Place(id=place_id, **data)
        data_manager.update(updated_place)
        return jsonify({'message': 'Place updated successfully'}), 200
    else:
        return jsonify({'message': 'Place not found'}), 404


@place_routes.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """
    Delete a specific place.

    Args:
        place_id (str): ID of the place to delete.

    Returns:
        JSON: JSON response indicating success
        or failure of the delete operation.
    """
    if not data_manager.place_exists(place_id):
        return jsonify({'message': 'Place not found'}), 404

    data_manager.delete(place_id, 'place')
    return jsonify({'message': 'Place deleted successfully'}), 204
