#!/usr/bin/python3
""" setup the app  for the api """

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
        404:
    description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.teardown_appcontext
def close_storage(exception):
    """ close the storage """
    storage.close()


if __name__ == "__main__":
    apiHost = getenv('HBNB_API_HOST', default='0.0.0.0')
    apiPort = getenv('HBNB_API_PORT', default='5000')
    app.run(host=apiHost, port=apiPort, threaded=True)
