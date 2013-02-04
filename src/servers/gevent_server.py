#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from flask import Flask, jsonify

app = Flask(__name__)
app.debug = False

QUERY_SPARQL_TEMPLATE = """
select * from <http://semantica.globo.com/> where {<http://semantica.globo.com/base/%s}> ?p ?o} LIMIT 100
"""

@app.route('/schemas/<ctx>/<entity>')
def get_class(ctx, entity):
    query = QUERY_SPARQL_TEMPLATE % entity
    response = {"ok":"belex"}
    return jsonify(response)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
