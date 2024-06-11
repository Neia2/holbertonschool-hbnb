#!/usr/bin/python3
"""
Review model
"""

from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'place': self.place_id,
            'rating': self.rating,
            'comment': self.comment
        }
