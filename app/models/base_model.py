#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class represents a base model with attributes for ID,
    creation time, and last update time.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel.

        Attributes:
        - id (str):
        A unique identifier generated using uuid4().
        - created_at (datetime):
        The date and time when the instance was created.
        - updated_at (datetime):
        The date and time when the instance was last updated,
        initially set to the creation time.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        # Method to update the last modified date and time
        self.updated_at = datetime.now()

    def update(self):
        # Method to update the last modified date and time (similar to save())
        self.updated_at = datetime.now()
