# api/v1/__init__.py
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# Import views to register routes with the blueprint
from api.v1.views.places import *
from api.v1.views.country_city_routes import *
from api.v1.views.amenity_routes import *
from api.v1 import app_views
app.register_blueprint(app_views)