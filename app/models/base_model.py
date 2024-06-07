#!/usr/bin/python3
"""
Base_model
"""

import uuid 
from datetime import datetime 

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update(self):
        self.updated_at = datetime.now()
