#!/usr/bin/python3
"""
Amenity model
"""

from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        self.name = name
