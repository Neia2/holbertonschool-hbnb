#!/usr/bin/python3

from flask import Flask
from app.routes.country_city_routes import country_city_routes
from app.routes.user_routes import user_routes
from app.routes.place_routes import place_routes

app = Flask(__name__)
app.register_blueprint(country_city_routes)
app.register_blueprint(user_routes)
app.register_blueprint(place_routes)

@app.route('/')
def index():
    return 'Welcome to the Country and City API'


if __name__ == '__main__':
    app.run(debug=True)
