#!/usr/bin/python3
""""index page to display status of the api"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return status of the api"""
    return jsonify({"status": "OK"})
