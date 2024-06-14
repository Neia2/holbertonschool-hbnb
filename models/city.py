#!/usr/bin/python3

class City:
    def __init__(self, id, name, country_code, created_at, updated_at):
        self.id = id
        self.name = name
        self.country_code = country_code
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
