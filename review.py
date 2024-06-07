import uuid

class Review:
    def __init__(self, user_id, place_id, rating, comment):
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
