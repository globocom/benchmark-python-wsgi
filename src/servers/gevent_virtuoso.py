#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

import requests
from flask import Flask, json

from settings import SPARQL_ENDPOINT
from queries import GET_QUERY

app = Flask(__name__)
app.debug = False


@app.route('/')
def get():
    payload = {
        "query": GET_QUERY,
        "format": "application/sparql-results+json"
    }
    r = requests.get(SPARQL_ENDPOINT, params=payload)
    return r.text


if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
