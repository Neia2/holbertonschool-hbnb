#!/usr/bin/python3
"""
City model
"""

from .base_model import BaseModel
import uuid
from datetime import datetime 

class City(BaseModel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'country_id': self.country_id
        }