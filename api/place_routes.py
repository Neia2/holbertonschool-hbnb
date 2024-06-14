# api/place_routes.py

from flask import Blueprint, jsonify, request, abort
from models import storage
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.user import User

place_routes = Blueprint('place_routes', __name__)

@place_routes.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    required_fields = ['name', 'description', 'address', 'city_id', 'latitude', 'longitude', 'host_id', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing {field}")
    
    city = storage.get(City, data['city_id'])
    if not city:
        abort(404, description="City not found")
    
    host = storage.get(User, data['host_id'])
    if not host:
        abort(404, description="Host not found")
    
    amenities = []
    if 'amenity_ids' in data:
        for amenity_id in data['amenity_ids']:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                amenities.append(amenity)
            else:
                abort(404, description=f"Amenity {amenity_id} not found")

    new_place = Place(**data)
    for amenity in amenities:
        new_place.add_amenity(amenity)
    
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201

@place_routes.route('/places', methods=['GET'])
def get_places():
    places = storage.all(Place).values()
    return jsonify([place.to_dict() for place in places])

@place_routes.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())

@place_routes.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'city_id']:
            setattr(place, key, value)
    
    if 'amenity_ids' in data:
        place.amenities = []
        for amenity_id in data['amenity_ids']:
            amenity = storage.get(Amenity, amenity_id)
            if amenity:
                place.add_amenity(amenity)
            else:
                abort(404, description=f"Amenity {amenity_id} not found")
    
    storage.save()
    return jsonify(place.to_dict()), 200

@place_routes.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    
    storage.delete(place)
    storage.save()
    return jsonify({}), 204
