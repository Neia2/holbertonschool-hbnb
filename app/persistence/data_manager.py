#!/usr/bin/python3
"""
Data Manager
"""
from .ipersistence_manager import IPersistenceManager
from datetime import datetime
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
            json.dump(self.data, file, default=self._json_serial)

    def _json_serial(self, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {obj} not serializable")

    def save(self, entity):
        entity_type = type(entity).__name__.lower()
        if entity_type not in self.data:
            self.data[entity_type] = []
        self.data[entity_type].append(entity.__dict__)
        self._save_data()

    def get(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        for entity in self.data.get(entity_type, []):
            if entity['id'] == entity_id:
                return entity
        return None

    def get_all(self, entity_type):
        if (entity_type in self.data):
            return list(self.data[entity_type].values())
        return []

    def update(self, entity):
        entity_type = type(entity).__name__.lower()
        entities = self.data.get(entity_type, [])
        for i, existing_entity in enumerate(entities):
            if existing_entity['id'] == entity.id:
                entities[i] = entity.__dict__
                break
        self._save_data()

    def delete(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        entities = self.data.get(entity_type, [])
        self.data[entity_type] = [e for e in entities if e['id'] != entity_id]
        self._save_data()
