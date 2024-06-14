# api/app.py

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from api.country_city_routes import country_ns, city_ns
from api.amenity_routes import amenity_ns
from api.place_routes import place_ns  # Import the new place namespace

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

api.add_namespace(country_ns)
api.add_namespace(city_ns)
api.add_namespace(amenity_ns)
api.add_namespace(place_ns)  # Add the new place namespace

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
