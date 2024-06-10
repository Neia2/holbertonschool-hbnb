from datetime import datetime
import uuid

class User:
    def __init__(self, email, name, password):
        self.id = str(uuid.uuid4())
        self.email = email
        self.name = name
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

@classmethod
    def is_email_unique(cls, email, users):
        for user in users:
            if user.email == email:
                return False
        return True