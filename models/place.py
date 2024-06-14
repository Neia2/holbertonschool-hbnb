# models/place.py

from datetime import datetime
import uuid
from models.city import City
from models.amenity import Amenity
from models.user import User

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids=[]):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.host_id = host_id
        self.amenity_ids = amenity_ids
        self.reviews = []
        self.amenities = []
        self.host = None

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def set_host(self, host):
        if not isinstance(host, User):
            raise Exception("Invalid host type.")
        self.host = host

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'host_id': self.host_id,
            'amenity_ids': self.amenity_ids,
            'city': self.get_city(),
            'amenities': [amenity.to_dict() for amenity in self.amenities]
        }

    def get_city(self):
        return storage.get(City, self.city_id).to_dict()
