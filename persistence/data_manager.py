from persistence.i_persistence_manager import IPersistenceManager

import json
import os

class DataManager(IPersistenceManager):
    def __init__(self, storage_path='data.json'):
        self.storage_path = storage_path
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        return {}

    def _save_data(self):
        with open(self.storage_path, 'w') as file:
            json.dump(self.data, file)

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity.id] = entity.__dict__
        self._save_data()

    def get(self, entity_id, entity_type):
        if entity_type in self.data and entity_id in self.data[entity_type]:
            return self.data[entity_type][entity_id]
        return None

    def get_all(self, entity_type):
        if entity_type in self.data:
            return list(self.data[entity_type].values())
        return []

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.data and entity.id in self.data[entity_type]:
            self.data[entity_type][entity.id] = entity.__dict__
            self._save_data()

    def delete(self, entity_id, entity_type):
        if entity_type in self.data and entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]
            self._save_data()
