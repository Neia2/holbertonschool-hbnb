#!/usr/bin/python3
"""
Place model

This module defines the Place class which inherits from BaseModel.
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Place class represents a place entity.

    Attributes:
        name (str): The name of the place.
        description (str): Description of the place.
        address (str): Address of the place.
        city_id (str): ID of the city where the place is located.
        host_id (str): ID of the host who manages the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        num_rooms (int): Number of rooms in the place.
        num_bathrooms (int): Number of bathrooms in the place.
        price_per_night (float): Price per night to stay at the place.
        max_guests (int): Maximum number of guests allowed in the place.
    """

    def __init__(self, name, description, address, city_id,
                 latitude, longitude, host_id, num_rooms,
                 num_bathrooms, price_per_night, max_guest):
        """
        Initialize a new Place instance.

        Args:
            name (str): The name of the place.
            description (str): Description of the place.
            address (str): Address of the place.
            city_id (str): ID of the city where the place is located.
            host_id (str): ID of the host who manages the place.
            latitude (float): Latitude coordinate of the place.
            longitude (float): Longitude coordinate of the place.
            num_rooms (int): Number of rooms in the place.
            num_bathrooms (int): Number of bathrooms in the place.
            price_per_night (float): Price per night to stay at the place.
            max_guests (int): Maximum number of guests allowed in the place.
        """
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
        """
        Convert the Place object to a dictionary representation.

        Returns:
        Dictionary containing the id, created_at, updated_at,
        and all attributes of the place.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'host_id': self.host_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'num_rooms': self.num_rooms,
            'num_bathrooms': self.num_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests
        }
