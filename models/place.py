from datetime import datetime
import uuid

class Place:
    def __init__(self, name, description, latitude, longitude, price_per_night, max_guests, host):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.host = host
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

		  def set_host(self, host):
        if not isinstance(self.host, User):
            self.host = host
        else:
            raise Exception("Place already has a host.")
