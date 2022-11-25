#!/usr/bin/python3
"""
view for State objects that handles all default RESTful API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """Retrieves all states"""
    state_list = []
    for state in storage.all(State).values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id=None):
    """Retrieves a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)  # a 404 error
    else:
        return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id=None):
    """Deletes a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)  # a 404 error
    else:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a state"""
    request = request.get_json(silent=True)
    if request is None:
        abort(400, "Not a JSON")
    elif 'name' not in request.keys():
        abort(400, "Missing name")
    else:
        new_state = State(**request)
        storage.new(new_state)
        storage.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id=None):
    """Creates a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    update = request.get_json(silent=True)
    if update is None:
        abort(400, "Not a JSON")
    else:
        for key, value in update.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(state, key, value)
        storage.save()
        response = state.to_dict()
        return jsonify(response), 200
