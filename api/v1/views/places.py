# api/v1/views/places.py

from flask import jsonify, request, abort
from models import storage
from models.place import Place
from models.city import City
from models.amenity import Amenity
from api.v1.views import app_views

@app_views.route('/places', methods=['POST'], strict_slashes=False)
def create_place():
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data or 'city_id' not in data:
        abort(400, description="Missing name or city_id")

    city = storage.get(City, data['city_id'])
    if not city:
        abort(404, description="City not found")

    if 'latitude' in data and not (-90 <= data['latitude'] <= 90):
        abort(400, description="Invalid latitude")
    if 'longitude' in data and not (-180 <= data['longitude'] <= 180):
        abort(400, description="Invalid longitude")

    if 'number_of_rooms' in data and data['number_of_rooms'] < 0:
        abort(400, description="Invalid number of rooms")
    if 'number_of_bathrooms' in data and data['number_of_bathrooms'] < 0:
        abort(400, description="Invalid number of bathrooms")
    if 'max_guests' in data and data['max_guests'] < 0:
        abort(400, description="Invalid max guests")
    if 'price_per_night' in data and data['price_per_night'] < 0:
        abort(400, description="Invalid price per night")

    new_place = Place(**data)
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201

@app_views.route('/places', methods=['GET'], strict_slashes=False)
def get_places():
    places = storage.all(Place).values()
    return jsonify([place.to_dict() for place in places])

@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
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
    
    storage.save()
    return jsonify(place.to_dict()), 200

@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    storage.delete(place)
    storage.save()
    return jsonify({}), 204
