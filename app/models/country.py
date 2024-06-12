#!/usr/bin/python3
"""
Country model
"""

from .base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'name': self.name,
            'code': self.code
        }