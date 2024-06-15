#!/usr/bin/python3
"""
This module defines the Country class which inherits from BaseModel.
"""

from .base_model import BaseModel


class Country(BaseModel):
    """
    Country class represents a country entity.

    Attributes:
    - name (str):
    The name of the country.
    - code (str):
    The code of the country.
    """
    def __init__(self, name, code):
        """
        Initialize a new Country instance.

        Args:
        name (str): The name of the country.
        code (str): The code of the country.
        """
        super().__init__()
        self.name = name
        self.code = code

    def to_dict(self):
        """
        Convert the Country object to a dictionary representation.

        Returns:
        Dictionary containing the id, created_at, updated_at,
        and all the attributes of the Country object.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name,
            'code': self.code
        }
