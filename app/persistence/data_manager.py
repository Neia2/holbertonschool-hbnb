#!/usr/bin/python3
"""
Data Manager
"""
from .ipersistence_manager import IPersistenceManager
from datetime import datetime
import json
import os


class DataManager(IPersistenceManager):
    """
    DataManager class implements the IPersistenceManager interface
    to provide data persistence using JSON files.
    """
    def __init__(self, storage_path='data.json'):
        """
        Initialize DataManager with a storage path for JSON data.

        Args:
        - storage_path (str):
        Path to the JSON storage file.
        """
        self.storage_path = storage_path
        self.data = self._load_data()

    def _load_data(self):
        """
        Load data from the JSON storage file.

        Returns:
        Loaded data from JSON file or an empty dictionary
        if file does not exist.
        """
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        return {}

    def _save_data(self):
        """
        Save current data to the JSON storage file.
        """
        with open(self.storage_path, 'w') as file:
            json.dump(self.data, file, default=self._json_serial)

    def _json_serial(self, obj):
        """
        JSON serializer for datetime objects.

        Args:
        - obj: Object to serialize.

        Returns:
        - str: ISO formatted string representation of datetime objects.

        Raises:
        - TypeError: If the object type is not serializable.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {obj} not serializable")

    def save(self, entity):
        """
        Save an entity to the JSON storage.

        Args:
        - entity: The entity object to save.
        """
        entity_type = type(entity).__name__.lower()
        if entity_type not in self.data:
            self.data[entity_type] = []
        self.data[entity_type].append(entity.__dict__)
        self._save_data()

    def get(self, entity_id, entity_type):
        """
        Get an entity from the JSON storage by its ID and type.

        Args:
        - entity_id (str): The ID of the entity.
        - entity_type (str): The type of entity.

        Returns:
        - dict or None: The entity dictionary if found, None otherwise.
        """
        entity_type = entity_type.lower()
        for entity in self.data.get(entity_type, []):
            if entity['id'] == entity_id:
                return entity
        return None

    def get_all(self, entity_type):
        """
        Get all entities of a specific type from the JSON storage.

        Args:
        - entity_type (str): The type of entities to retrieve.

        Returns:
        - list: List of entity dictionaries.
        """
        if (entity_type in self.data):
            return list(self.data[entity_type].values())
        return []

    def update(self, entity):
        """
        Update an entity in the JSON storage.

        Args:
        - entity: The entity object to update.
        """
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
