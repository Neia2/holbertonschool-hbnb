#!/usr/bin/python3
"""
This module defines the Review class which inherits from BaseModel.
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a review entity.

    Attributes:
    - user_id (str):
      ID of the user who wrote the review.
    - place_id (str):
      ID of the place being reviewed.
    - rating (float):
      Rating given by the user for the place.
    - comment (str):
      Optional comment provided by the user.
    """
    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        """
        Convert the Review object to a dictionary representation.

        Returns:
        Dictionary containing the attributes of the Review object.
        """
        return {
            'id': str(self.id),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'place': self.place_id,
            'rating': self.rating,
            'comment': self.comment
        }
