#!/usr/bin/python3
"""
Country model
"""

from .base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, code):
        self.name = name
        self.code = code
