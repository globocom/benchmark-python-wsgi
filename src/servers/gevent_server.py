#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from flask import Flask
import geventredis

app = Flask(__name__)
app.debug = False


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
