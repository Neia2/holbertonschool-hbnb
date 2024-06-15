#!/usr/bin/python3

"""
Routes Package Initialization

This script initializes a Flask application and registers various Blueprints
for different API endpoints related to managing users, reviews, places,
and country/city data.

Modules:
- country_city_routes: Routes for managing country and city data.
- user_routes: Routes for managing user data
(create, retrieve, update, delete).
- place_routes: Routes for managing place data
(create, retrieve, update, delete).
- review_routes: Routes for managing reviews associated with places or users.

Usage:
Import and register the blueprints from this package
with the Flask application.
Run the script to start the Flask application server.

Example:
from app.routes import country_city_routes,
user_routes, place_routes, review_routes

app = Flask(__name__)
app.register_blueprint(country_city_routes)
app.register_blueprint(user_routes)
app.register_blueprint(place_routes)
app.register_blueprint(review_routes)

if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask
from app.routes.country_city_routes import country_city_routes
from app.routes.user_routes import user_routes
from app.routes.place_routes import place_routes
from app.routes.review_routes import review_routes

app = Flask(__name__)

# Registering blueprints for different sets of routes
app.register_blueprint(country_city_routes)
app.register_blueprint(user_routes)
app.register_blueprint(place_routes)
app.register_blueprint(review_routes)


@app.route('/')
def index():
    """
    Home Route

    Returns a welcome message when the root URL is accessed.
    """
    return 'Welcome to the Country and City API'


if __name__ == '__main__':
    app.run(debug=True)
