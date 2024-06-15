#!/usr/bin/python3
"""
Persistence Manager Package Initialization

This package provides classes and interfaces for managing data persistence
in the application. It includes implementations for saving, retrieving,
updating, and deleting data.
"""

# Import DataManager class for handling data storage and retrieval
from .data_manager import DataManager

# Import interface to define the contract for persistence operations
from .ipersistence_manager import IPersistenceManager
