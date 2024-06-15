#!/usr/bin/python3
"""
This module defines the City class, which represents a city entity,
and inherits from BaseModel.
"""

from .base_model import BaseModel
import uuid
from datetime import datetime


class City(BaseModel):
    """
    City class represents a city entity with attributes for ID, name,
    country ID, creation time, and last update time.
    """

    def __init__(self, name, country_id):
        """
        Initializes a new instance of the City.

        Args:
        - name (str): The name of the city.
        - country_id (str): The ID of the country to which the city belongs.

        Attributes:
        - name (str):
        The name of the city.
        - country_id (str):
        The ID of the country to which the city belongs.
        """
        super().__init__()
        self.name = name
        self.country_id = country_id

    def to_dict(self):
        """
        Convert the City object to a dictionary representation.

        Returns:
        Dictionary containing the id, created_at, updated_at,
        and all the attributes of the City object.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name,
            'country_id': self.country_id
        }
