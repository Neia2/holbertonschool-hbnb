# api/v1/views/__init__.py

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.places import *
from api.v1.views.country_city_routes import *
from api.v1.views.amenity_routes import *
