#!/usr/bin/python3
"""
Amenity model
"""

from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name
        }
