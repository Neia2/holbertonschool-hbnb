from flask import Flask
from api.country_city_routes import country_city_routes
from .user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(country_city_routes)
app.register_blueprint(user_routes)

@app.route('/')
def index():
    return 'Welcome to the Country and City API'

if __name__ == '__main__':
    app.run(debug=True)
