#!/usr/bin/python3
"""
Persistence Manager Interface
"""
from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """
    Abstract base class for defining persistence operations.
    """

    @abstractmethod
    def save(self, entity):
        """
        Abstract method to save an entity.

        Args:
        - entity:
        The entity object to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Abstract method to get an entity by its ID.

        Args:
        - entity_id (str):
        The ID of the entity.
        - entity_type (str):
        The type of entity.

        Returns:
        The entity dictionary if found, None otherwise.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Abstract method to update an entity.

        Args:
        The entity object to be updated.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Abstract method to delete an entity.

        Args:
        - entity_id (str):
        The ID of the entity to delete.
        - entity_type (str):
        The type of entity.
        """
        pass
