# persistence/data_manager.py
import json
import os

class DataManager:
    def __init__(self):
        self.data = self._load_data()

    def _load_data(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'data.json')
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}
        except FileNotFoundError as e:
            print(f"JSON file not found: {e}")
            return {}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {}

    def get_data(self):
        return self.data

    def save(self, obj):
        if isinstance(obj, Country):
            if "countries" not in self.data:
                self.data["countries"] = []
            self.data["countries"].append(obj.to_dict())
        elif isinstance(obj, City):
            if "cities" not in self.data:
                self.data["cities"] = []
            self.data["cities"].append(obj.to_dict())
        self._save_data()

    def _save_data(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'data.json')
            with open(file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

<<<<<<< HEAD
class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code
=======
    def get_all(self, entity_type):
        if entity_type in self.data:
            return list(self.data[entity_type].values())
        return []

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.data and entity.id in self.data[entity_type]:
            self.data[entity_type][entity.id] = entity.__dict__
            self._save_data()
>>>>>>> origin/matrix

    def to_dict(self):
        return {
            "name": self.name,
            "code": self.code
        }

class City:
    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code

    def to_dict(self):
        return {
            "name": self.name,
            "country_code": self.country_code
        }
