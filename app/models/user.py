#!/usr/bin/python3
"""
This module defines the User class which inherits from BaseModel.
"""

from .base_model import BaseModel
import uuid
from datetime import datetime


class User(BaseModel):
    email_set = set()

    def __init__(self, email, first_name, last_name):
        """
    User class represents a user entity.

    Attributes:
    - email (str):
      Email address of the user.
    - first_name (str):
      First name of the user.
    - last_name (str):
      Last name of the user.
    """
        if email in User.email_set:
            raise Exception("Email already exists")

        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        User.email_set.add(email)
        self.save()

    def to_dict(self):
        """
        Convert the User object to a dictionary representation.

        Returns:
        Dictionary containing the attributes of the User object.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
