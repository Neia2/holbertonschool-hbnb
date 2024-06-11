#!/usr/bin/python3
"""
Place model
"""

from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, address, city_id,
                 latitude, longitude, host_id, num_rooms,
                 num_bathrooms, price_per_night, max_guest):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.host_id = host_id
        self.latitude = latitude
        self.longitude = longitude
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guest

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'adress': self.address,
            'city_id': self.city_id,
            'host_id': self.host_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'num_rooms': self.num_rooms,
            'num_bathrooms': self.num_bathrooms,
            'price_per_night': self.price_per_night,
            
        }
