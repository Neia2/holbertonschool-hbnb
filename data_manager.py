import json

class DataManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.data = {}

    def _load_data(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def _save_data(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file)

    def save(self, entity):
        entity_id = str(entity.id)
        entity_type = entity.__class__.__name__.lower()
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity_id] = entity.__dict__
        self._save_data()

    def get(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        return self.data.get(entity_type, {}).get(entity_id, None)

    def update(self, entity):
        entity_id = str(entity.id)
        entity_type = entity.__class__.__name__.lower()
        if entity_type in self.data and entity_id in self.data[entity_type]:
            self.data[entity_type][entity_id] = entity.__dict__
            self._save_data()

    def delete(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        if entity_type in self.data and entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]
            self._save_data()
