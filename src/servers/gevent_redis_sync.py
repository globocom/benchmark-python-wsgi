#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import geventredis

from flask import Flask

app = Flask(__name__)
app.debug = False

redis_client = redis.Redis(host="localhost", port=6379)

@app.route('/redis')
def get():
    result = redis_client.get("foo")
    return result

@app.route('/redis')
def post():
    result = redis_client.post("foo", "bar")
    return result

@app.route('/redis')
def delete():
    result = redis_client.delete("foo")
    return result

if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()
