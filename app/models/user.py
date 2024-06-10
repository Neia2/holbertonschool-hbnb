#!/usr/bin/python3
"""
User model
"""

from .base_model import BaseModel
import uuid
from datetime import datetime 

class User(BaseModel):
    email_set = set()

    def __init__(self, email, first_name, last_name):
        if email in User.email_set:
            raise ValueError("Email already exists")

        self.email = email 
        self.first_name = first_name
        self.last_name = last_name
        User.email_set.add(email)
        self.save()
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

