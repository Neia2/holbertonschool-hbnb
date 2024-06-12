# api/app.py
from flask import Flask
from flask_restx import Api
from api.country_city_routes import country_ns, city_ns
from api.db import app, db  # Correct import here

app = Flask(__name__)
api = Api(app)

api.add_namespace(country_ns)
api.add_namespace(city_ns)

@app.route('/')
def index():
    return 'Welcome to the Country and City API'

if __name__ == '__main__':
    app.run(debug=True)
