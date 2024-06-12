# load_countries.py
from api.app import db, app
from models.country import Country

countries = [
    {'code': 'US', 'name': 'United States'},
    {'code': 'CA', 'name': 'Canada'},
    # Add more countries as needed
]

def load_countries():
    for country_data in countries:
        country = Country(code=country_data['code'], name=country_data['name'])
        db.session.add(country)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        load_countries()
