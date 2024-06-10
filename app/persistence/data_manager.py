#!/usr/bin/python3
"""
Data Manager
"""

from datetime import datetime
from .ipersistence_manager import IPersistenceManager
import json

class DataManager(IPersistenceManager):
    def __init__(self, storage_file, data):
        self.storage_file = storage_file
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_data(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.data, f, default=self._json_serializer)

    def _json_serializer(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj.__dict__

    def save(self, entity):
        entity_type = type(entity).__name__.lower()
        if entity_type not in self.data:
            self.data[entity_type] = []
        self.data[entity_type].append(entity.to_dict())
        self._save_data()

    def get(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        for entity in self.data.get(entity_type, []):
            if entity['id'] == entity_id:
                return entity
        return None

    def update(self, entity):
        entity_type = type(entity).__name__.lower()
        entities = self.data.get(entity_type, [])
        for i, existing_entity in enumerate(entities):
            if existing_entity['id'] == entity.id:
                entities[i] = entity.to_dict()
                break
        self._save_data()

    def delete(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        entities = self.data.get(entity_type, [])
        self.data[entity_type] = [e for e in entities if e['id'] != entity_id]
        self._save_data()
