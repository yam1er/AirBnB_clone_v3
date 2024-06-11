#!/usr/bin/python3
'''
Create Flask app views
'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
        call status
    """
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stat():
    """Give class stats"""
    response = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(response)
