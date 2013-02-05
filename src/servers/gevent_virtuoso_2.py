#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from gevent import monkey
monkey.patch_all()

import requests
from flask import Flask, json

from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

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


    url = URL('https://graph.facebook.com/me/friends')
    http_client = HTTPClient.from_url(url, concurrency=1)
    response = http_client.get(url.request_uri)
    assert response.status_code == 200
    result_dict = json.load(response)['data']
    pretty_json_string = json.dumps(result_dict, sort_keys=True, indent=4, separators=(",", ":"))


if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
