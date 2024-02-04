#!/usr/bin/python3
""""index page to display status of the api"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return status of the api"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """return stats of the api"""
    classes = {"amenities": "Amenity", "cities": "City","places": "Place",
               "reviews": "Review", "states": "Satet", "users": "User"}
    statsCls = {}
    for key, value in classes.items():
        statsCls[key] = storage.count(value)
    return jsonify(statsCls)
