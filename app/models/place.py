#!/usr/bin/python3
"""
Place model
"""

from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, address, city_id,
                 latitude, longitude, host_id, num_rooms,
                 num_bathrooms, price_per_night, max_guest):
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
        self.max_guests = max_guests
