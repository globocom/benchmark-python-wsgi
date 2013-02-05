#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib

from gevent.wsgi import WSGIServer

from flask import Flask

from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

from geventhttpclient import httplib
httplib.patch()
from httplib2 import Http

import sys
sys.path.insert(0, "/Users/rodrigo.senra/r/projects/benchmark-python-wsgi/src")

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
    params = urllib.urlencode(payload)
    url = URL(SPARQL_ENDPOINT + "?"+ params)

    http = Http()
    response, content = http.request(SPARQL_ENDPOINT + "?"+ params)
    return content

#    http_client = HTTPClient.from_url(url, concurrency=1)
#    response = http_client.get(url.request_uri)
#    return response

if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
