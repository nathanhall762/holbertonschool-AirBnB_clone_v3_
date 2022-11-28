#!/usr/bin/python3
"""
view for place objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models import storage
from models.place import Place


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def all_places():
    """Retrieves all places"""
    #  if:  # exists
    #    return jsonify({})  # return all place objects
    abort(404)  # a 404 error


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id=None):
    """Retrieves a place"""
    s = storage.get(Place, place_id)
    if s is None:
        abort(404)  # a 404 error
    return jsonify(s.to_dict()), 200


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place():
    """Deletes a place"""
    #  if:  # id is linked to a place object
    #    return jsonify({})  # return all place objects
    #  if:  # id is linked to an empty place object
    #    return  # empty dictionary
    abort(404)  # a 404 error


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place():
    """Creates a place"""
    abort(404)  # a 404 error


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place():
    """Creates a place"""
    abort(404)  # a 404 error
