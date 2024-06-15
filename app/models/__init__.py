#!/usr/bin/python3
"""
Package Initialization

This package contains the core models used in the application, including
the base model and various entity models such as User, Place, Review,
Country, City, and Amenity.

Version:
    1.0.0
"""

# Version du package
__version__ = "1.0.0"

# Import base model and entity models
from .base_model import BaseModel  # Base class for all models
from .user import User  # User model representing application users
from .place import Place  # Place model representing rental places
from .review import Review  # Review model representing user reviews for places
from .country import Country  # Country model representing countries
from .city import City  # City model representing cities
# Amenity model representing amenities associated with places
from .amenity import Amenity
