# models/storage.py

from models import db

class Storage:
    def all(self, cls):
        return db.session.query(cls).all()

    def get(self, cls, id):
        return db.session.query(cls).get(id)

    def new(self, obj):
        db.session.add(obj)

    def save(self):
        db.session.commit()

    def delete(self, obj):
        db.session.delete(obj)
        db.session.commit()

storage = Storage()
