#!/usr/bin/python3

from flask import request
from flask_restx import Namespace, Resource, fields
from models.amenity import Amenity, db

amenity_ns = Namespace('amenities', description='Amenity operations')

amenity_model = amenity_ns.model('Amenity', {
    'id': fields.Integer(readonly=True, description='The amenity unique identifier'),
    'name': fields.String(required=True, description='The amenity name'),
    'created_at': fields.DateTime(readonly=True),
    'updated_at': fields.DateTime(readonly=True)
})

@amenity_ns.route('/')
class AmenityList(Resource):
    @amenity_ns.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        amenities = Amenity.query.all()
        return [amenity.to_dict() for amenity in amenities], 200

    @amenity_ns.expect(amenity_model)
    @amenity_ns.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = request.json
        if 'name' not in data or not data['name']:
            return {'message': 'Amenity name is required'}, 400
        if Amenity.query.filter_by(name=data['name']).first():
            return {'message': 'Amenity name must be unique'}, 409

        new_amenity = Amenity(name=data['name'])
        db.session.add(new_amenity)
        db.session.commit()
        return new_amenity.to_dict(), 201

@amenity_ns.route('/<int:id>')
class AmenityResource(Resource):
    @amenity_ns.marshal_with(amenity_model)
    def get(self, id):
        """Fetch a single amenity"""
        amenity = Amenity.query.get_or_404(id)
        return amenity.to_dict(), 200

    @amenity_ns.expect(amenity_model)
    @amenity_ns.marshal_with(amenity_model)
    def put(self, id):
        """Update an amenity"""
        amenity = Amenity.query.get_or_404(id)
        data = request.json
        if 'name' in data:
            if not data['name']:
                return {'message': 'Amenity name cannot be empty'}, 400
            if Amenity.query.filter_by(name=data['name']).first():
                return {'message': 'Amenity name must be unique'}, 409
            amenity.name = data['name']
        db.session.commit()
        return amenity.to_dict(), 200

    def delete(self, id):
        """Delete an amenity"""
        amenity = Amenity.query.get_or_404(id)
        db.session.delete(amenity)
        db.session.commit()
        return '', 204