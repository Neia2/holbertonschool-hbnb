#!/usr/bin/python3

from flask import Flask
from app.routes.amenity_routes
from app.routes.city_routes
from app.routes.country_routes
from app.routes.place_routes
from app.routes.review_routes
from app.routes.user_routes 

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(content_bp)
