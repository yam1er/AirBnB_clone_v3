#!/usr/bin/python3
'''
Flask app creation and register the blueprint app_views to flask intance
'''
from api.v1.views import app_views
from flask import Flask
from os import getenv
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")

@app.teardown_appcontext
def close_db(exception):
    storage.close()

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
