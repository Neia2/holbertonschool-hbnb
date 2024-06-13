# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models here to register them with SQLAlchemy
from models.amenity import Amenity
# Add other models here as needed
