# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models here to register them with SQLAlchemy
from models.amenity import Amenity
from .user import User
from .place import Place
# Add other models here as needed
