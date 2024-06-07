#!/usr/bin/python3
"""
City model
"""

from .base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id
