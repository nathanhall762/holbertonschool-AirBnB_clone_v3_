#!/usr/bin/python3
"""Flask app startup"""
from flask import Flask
from models import storage
from api.v1.view import app_views


app = Flask(__name__)


@app.route('/')
def

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=int(port), threaded=True)
