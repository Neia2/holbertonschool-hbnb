from datetime import datetime
import uuid
from persistence.data_manager import DataManager

class User:
    def __init__(self, email, full_name, password):
        self.id = str(uuid.uuid4())
        self.email = email
        self.full_name = full_name
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        DataManager().save(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
        self.save()
