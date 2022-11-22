#!/usr/bin/python3
"""
view for City objects that handles all default RESTful API actions
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/api/v1/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def all_cities():
    """Retrieves all cities"""
    if:  # exists
        return jsonify({})  # return all city objects
    return  # a 404 error


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city():
    """Retrieves a city"""
    if:  # id is linked to a city object
        return jsonify({})  # return city object of city_id
    return  # a 404 error


@app_views.route('/api/v1/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city():
    """Deletes a city"""
    if:  # id is linked to a city object
        return jsonify({})  # return all city objects
    if:  # id is linked to an empty city object
        return  # empty dictionary
    return  # a 404 error


@app_views.route('/api/v1/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city():
    """Creates a city"""
    return  # a 404 error


@app_views.route('/api/v1/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city():
    """Creates a city"""
    return  # a 404 error
