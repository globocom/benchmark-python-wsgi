#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import httpclient

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.httputil import url_concat

from flask import Flask, jsonify


app = Flask(__name__)
app.debug = False

SPARQL_ENDPOINT = "http://localhost:8890/sparql"

QUERY_SPARQL_TEMPLATE = """
select * from <http://semantica.globo.com/> where {<http://semantica.globo.com/base/%s}> ?p ?o} LIMIT 100
"""

http_client = httpclient.AsyncHTTPClient()

def handle_request(response):
    if response.error:
        print "Error:", response.error
        #ioloop.IOLoop.instance().stop()
    else:
        print response.body


@app.route('/schemas/<ctx>/<entity>')
def get_class(ctx, entity):
    query = QUERY_SPARQL_TEMPLATE % entity
    url = url_concat(SPARQL_ENDPOINT, {"query": query})
    http_client.fetch(url, handle_request)
    response = {"ok":"belex"}
    return jsonify(response)

@app.route('/')
def hello_world():
    print "\na"
    return 'Hello World!'

if __name__=="__main__":
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8888)
    IOLoop.instance().start()
