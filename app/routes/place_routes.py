#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from models.place import Place
from models.amenity import Amenity
from persistence.data_manager import DataManager

place_routes = Blueprint('place_routes', __name__)
data_manager = DataManager()

@place_routes.route('/places', methods=['POST'])
def create_place(self):
    data = request.json
    # Vérifier que les coordonnées géographiques sont valides
    if not (-90 <= data.get('latitude', 0) <= 90) or not (-180 <= data.get('longitude', 0) <= 180):
        return jsonify({'message': 'Invalid geographical coordinates'}), 400
    
    # Vérifier que le nombre de chambres, de salles de bains et de capacité de clients est un entier non négatif
    if not all(isinstance(data.get(field, 0), int) and data.get(field, 0) >= 0 for field in ['num_rooms', 'num_bathrooms', 'max_guests']):
        return jsonify({'message': 'Number of rooms, bathrooms, and max guests must be non-negative integers'}), 400
    
    # Vérifier que le prix par nuit est une valeur numérique valide
    if not isinstance(data.get('price_per_night', 0), (int, float)) or data.get('price_per_night', 0) < 0:
        return jsonify({'message': 'Price per night must be a valid non-negative numerical value'}), 400
    
    # Vérifier que city_id correspond à une ville existante dans la base de données
    city_id = data.get('city_id')
    city = data_manager.get(city_id, 'city')
    if not city:
        return jsonify({'message': 'Invalid city_id. City does not exist'}), 400

    # Vérifier que tous les amenity_ids fournis existent dans la base de données
    if 'amenity_ids' in data:
        invalid_amenities = [amenity_id for amenity_id in data['amenity_ids'] if not Amenity.query.filter_by(id=amenity_id).first()]
    if invalid_amenities:
        return jsonify({'message': f'Amenities with IDs {invalid_amenities} do not exist'}), 400
    
    # Si toutes les vérifications passent, créer un nouveau lieu
    place = Place(name=data['name'], description=data['description'], address=data['address'], 
                  city_id=data['city_id'], host_id=data['host_id'], latitude=data['latitude'],
                  longitude=data['longitude'], num_rooms=data['num_rooms'], num_bathrooms=data['num_bathrooms'],
                  price_per_night=data['price_per_night'], max_guests=data['max_guests'])
    data_manager.save(place)
    return jsonify(place.to_dict()), 201

# Retrieve a list of all places
@place_routes.route('/places', methods=['GET'])
def get_all_places():
    all_places = data_manager.get_all('place')
    return jsonify(all_places), 200

# Retrieve detailed information about a specific place
@place_routes.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, 'place')
    if place:
        return jsonify(place), 200
    else:
        return jsonify({'message': 'Place not found'}), 404

# Update an existing place’s information
@place_routes.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json
    place = data_manager.get(place_id, 'place')
    if place:
        updated_place = Place(id=place_id, **data)
        data_manager.update(updated_place)
        return jsonify({'message': 'Place updated successfully'}), 200
    else:
        return jsonify({'message': 'Place not found'}), 404

# Delete a specific place
@place_routes.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    data_manager.delete(place_id, 'place')
    return jsonify({'message': 'Place deleted successfully'}), 204