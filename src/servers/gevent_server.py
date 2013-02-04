#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = False


@app.route('/schemas/<ctx>/<entity>')
def get_class(ctx, entity):
    response = {"ok":"belex"}
    return jsonify(response)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
