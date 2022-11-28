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
    places = storage.get(City, city_id)
    places_list = []
    for place in places:
        places_list.append(place.to_dict())
    return jsonify(place_list)


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
def delete_place(place_id=None):
    """Deletes a place"""
    s = storage.get(Place, place_id)
    if s is not None:
        storage.delete(s)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)  # a 404 error


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place():
    """Creates a place"""
    req = request.get_json(silent=True)
    if req is None:
        abort(400, "Not a JSON")
    if 'name' not in req.keys():
        abort(400, "Missing name")
    new_place = Place(**req)
    storage.new(new_place)
    storage.save()
    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place(place_id=None):
    """Creates a place"""
    s = storage.get(Place, place_id)
    if s is None:
        abort(404)
    update = request.get_json(silent=True)
    if update is None:
        abort(400, "Not a JSON")
    else:
        for key, value in update.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(s, key, value)
        storage.save()
        response = s.to_dict()
        return make_response(jsonify(response), 200)
