#!/usr/bin/python3

from flask import Blueprint, request, jsonify
from app.models.review import Review
from app.models.user import User
from app.models.place import Place
from app.persistence.data_manager import DataManager

review_routes = Blueprint('review_routes', __name__)
data_manager = DataManager()

@review_routes.route('/places', methods=['POST'])
def create_place(self):
    data = request.json
    user_id = data.get('user_id')
    place_id = data.get('place_id')
    rating = data.get('rating')
    comment = data.get('comment')

    if not all([user_id, place_id, rating, comment]):
        return jsonify({'message': 'Missing user_id, place_id, rating, or comment'}), 400
    
    if not (1 <= rating <= 5):
        return jsonify({'message': 'Rating must be between 1 and 5'}), 400
    
    if not data_manager.user_exists(user_id):
        return jsonify({'message': 'Invalid user_id'}), 400

    if not data_manager.place_exists(place_id):
        return jsonify({'message': 'Invalid place_id'}), 400

    # Prevent hosts from reviewing their own places
    place = data_manager.get(place_id, 'place')
    if place['host_id'] == user_id:
        return jsonify({'message': 'Hosts cannot review their own place'}), 400

    review = Review(place_id=place_id, user_id=user_id, rating=rating, comment=comment)
    data_manager.save(review)
    return jsonify(review.to_dict()), 201

@review_routes.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    if not data_manager.user_exists(user_id):
        return jsonify({'message': 'User not found'}), 404

    reviews = [review for review in data_manager.get_all('review') if review['user_id'] == user_id]
    return jsonify(reviews), 200

@review_routes.route('/places/<place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    if not data_manager.place_exists(place_id):
        return jsonify({'message': 'Place not found'}), 404

    reviews = [review for review in data_manager.get_all('review') if review['place_id'] == place_id]
    return jsonify(reviews), 200

@review_routes.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    review = data_manager.get(review_id, 'review')
    if review:
        return jsonify(review), 200
    else:
        return jsonify({'message': 'Review not found'}), 404

@review_routes.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    review = data_manager.get(review_id, 'review')
    if not review:
        return jsonify({'message': 'Review not found'}), 404

    if 'rating' in data and not (1 <= data['rating'] <= 5):
        return jsonify({'message': 'Rating must be between 1 and 5'}), 400

    for key, value in data.items():
        if key in review:
            review[key] = value
    data_manager.update(review)
    return jsonify({'message': 'Review updated successfully'}), 200

@review_routes.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    if not data_manager.review_exists(review_id):
        return jsonify({'message': 'Review not found'}), 404

    data_manager.delete(review_id, 'review')
    return jsonify({'message': 'Review deleted successfully'}), 204
