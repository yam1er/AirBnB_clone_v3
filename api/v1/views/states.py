#!/usr/bin/python3
"""
  This module handle all REST API actions for State
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage


states = [state.to_dict() for state in storage.all("State")]


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    state = [state for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    return jsonify(state[0])


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = [state for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    obj = storage.get("State", state[0]['id'])
    storage.delete(obj)
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Create state object"""
    if not request.json:
        abort(400)
    return make_response(jsonify({}), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Update a State object"""
    state = [state for state in states if state['id'] == state_id]
    if len(state):
        abort(404)
    return make_response(jsonify({}), 200)
