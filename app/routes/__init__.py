"""
Routes Package Initialization

This package initializes Flask Blueprints for different API endpoints.
Each Blueprint represents a set of related routes for managing different
entities or operations within the application.

Modules:
- user_routes: Routes for managing user data (create, retrieve, update, delete).
- review_routes: Routes for managing reviews associated with places or users.
- place_routes: Routes for managing place data (create, retrieve, update, delete).
- country_city_routes: Routes for managing country and city data.
- amenity_ns: Namespace and routes for managing amenities using Flask-RESTx.

Usage:
Import the blueprints from this package and register them with the Flask application.

Example:
from app.routes import user_routes, review_routes, place_routes, country_city_routes, amenity_ns

app.register_blueprint(user_routes)
app.register_blueprint(review_routes)
app.register_blueprint(place_routes)
app.register_blueprint(country_city_routes)
app.register_blueprint(amenity_ns)
"""

from .user_routes import user_routes
from .review_routes import review_routes
from .place_routes import place_routes
from .country_city_routes import country_city_routes
from .amenity_routes import amenity_ns
