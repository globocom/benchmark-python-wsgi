#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gevent.wsgi import WSGIServer

def application(env, start_response):
    method = env['REQUEST_METHOD']
    path = env['PATH_INFO']
    path = path.lstrip('/')
    if (method, path) == ('GET', ''):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return ['Hello World!']


if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), application)
    http_server.serve_forever()

