#!/usr/bin/python3
"""
This module defines the Amenity class which inherits from BaseModel.
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents an amenity entity.

    Attributes:
    - name (str):
    The name of the amenity.
    """
    def __init__(self, name):
        """
        Initialize a new Amenity instance.

        Args:
        - name (str):
        The name of the amenity.
        """
        super().__init__()
        self.name = name

    def to_dict(self):
        """
        Convert the Amenity object to a dictionary representation.

        Returns:
        Dictionary containing the id, created_at, updated_at,
        and all the attributes of the Amenity object.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name
        }
