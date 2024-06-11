#!/usr/bin/python3

from flask import Flask
from app.routes.amenity_routes import Amenity_routes
from app.routes.city_routes import City_routes
from app.routes.country_routes import Country_routes
from app.routes.place_routes import Place_routes
from app.routes.review_routes import Review_routes
from app.routes.user_routes import User_routes

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(content_bp)
