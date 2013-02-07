Tornado retornando “Hello World!” na rede corporativa
-----------------------------------------------------

    <code>
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
    
    @app.route('/')
    def hello_world():
        print ".", # esta linha foi removida em um dos cenários
        return 'Hello World!'
    
    if __name__=="__main__":
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(8888)
        IOLoop.instance().start()
    
    </code>

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    36.43ms   35.17ms 237.48ms   91.88%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 7.17s, 1.14MB read
Requests/sec:   1395.30
Transfer/sec:    163.51KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    25.20ms    7.37ms  51.52ms   71.43%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 5.11s, 1.14MB read
Requests/sec:   1956.24
Transfer/sec:    229.25KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.81ms    5.86ms  52.28ms   67.10%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 4.68s, 1.14MB read
Requests/sec:   2137.54
Transfer/sec:    250.49KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    28.56ms   10.18ms  83.10ms   81.32%
    Req/Sec     0.00      0.00     0.00    100.00%
  10006 requests in 5.55s, 1.15MB read
Requests/sec:   1802.59
Transfer/sec:    211.24KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    26.83ms    9.41ms  70.45ms   79.17%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 5.29s, 1.14MB read
Requests/sec:   1891.06
Transfer/sec:    221.61KB

Tornando rodando “Hello World” sem print na rede corporativa
-------------------------------------------------------------


wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    22.09ms    5.70ms  46.52ms   76.43%
    Req/Sec     0.00      0.00     0.00    100.00%
  10010 requests in 4.67s, 1.15MB read
Requests/sec:   2145.75
Transfer/sec:    251.45KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    30.79ms    8.53ms  54.53ms   70.30%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 6.11s, 1.14MB read
Requests/sec:   1637.35
Transfer/sec:    191.88KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.72ms   10.01ms 100.80ms   88.27%
    Req/Sec     0.00      0.00     0.00    100.00%
  10008 requests in 4.94s, 1.15MB read
Requests/sec:   2026.90
Transfer/sec:    237.53KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    23.14ms    5.54ms  41.62ms   69.57%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 4.72s, 1.14MB read
Requests/sec:   2117.36
Transfer/sec:    248.13KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    22.55ms    5.06ms  42.13ms   78.43%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 4.57s, 1.14MB read
Requests/sec:   2186.74
Transfer/sec:    256.26KB

#-------------------------------------------------------
# Gevent retornando "Hello World" na rede da globo.com

<code>
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer
from flask import Flask

app = Flask(__name__)
app.debug = False

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    http_server = WSGIServer(('', 8888), app)
    http_server.serve_forever()

</code>


wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.26ms   15.50ms 266.76ms   96.08%
    Req/Sec     0.00      0.00     0.00    100.00%
  10004 requests in 11.29s, 1.71MB read
Requests/sec:    885.92
Transfer/sec:    154.86KB


wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    26.16ms   25.16ms 256.55ms   98.85%
    Req/Sec     0.00      0.00     0.00    100.00%
  10003 requests in 10.82s, 1.71MB read
Requests/sec:    924.46
Transfer/sec:    161.60KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    21.83ms    8.60ms  80.75ms   80.48%
    Req/Sec     0.00      0.00     0.00    100.00%
  10001 requests in 10.63s, 1.71MB read
Requests/sec:    941.02
Transfer/sec:    164.49KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.37ms   19.39ms 155.31ms   94.79%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 12.63s, 1.71MB read
Requests/sec:    791.95
Transfer/sec:    138.44KB


wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.29ms   30.52ms 372.54ms   94.65%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 11.46s, 1.71MB read
Requests/sec:    872.69
Transfer/sec:    152.55KB


#-------------------------------------------------------
# Gevent_virtuoso

<code>
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
</code>

wrk -r1000 -t2 -c5 http://X.X.X.22:8888/
Making 1000 requests to http://X.X.X.22:8888/
  2 threads and 5 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.49ms    3.31ms  21.95ms   65.85%
    Req/Sec     0.00      0.00     0.00    100.00%
  1000 requests in 6.16s, 344.73KB read
Requests/sec:    162.46
Transfer/sec:     56.00KB

wrk -r10000 -t5 -c50 "http://X.X.X.22:8888/"
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   295.27ms  581.73ms   3.60s    92.29%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 1.27m, 3.37MB read
  Socket errors: connect 0, read 0, write 0, timeout 256
Requests/sec:    130.91
Transfer/sec:     45.13KB

wrk -r10000 -t5 -c50 "http://X.X.X.22:8888/"
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   230.14ms  469.85ms   3.52s    95.45%
    Req/Sec     0.00      0.00     0.00    100.00%
  10005 requests in 1.18m, 3.37MB read
  Socket errors: connect 0, read 0, write 0, timeout 103
Requests/sec:    141.76
Transfer/sec:     48.87KB

wrk -r10000 -t5 -c50 "http://X.X.X.22:8888/"
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   231.35ms  436.76ms   3.59s    94.18%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 1.23m, 3.37MB read
  Socket errors: connect 0, read 0, write 0, timeout 178
Requests/sec:    135.03
Transfer/sec:     46.55KB

wrk -r10000 -t5 -c50 "http://X.X.X.22:8888/"
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   229.98ms  455.50ms   3.50s    95.36%
    Req/Sec     0.00      0.00     0.00    100.00%
  10003 requests in 1.22m, 3.37MB read
  Socket errors: connect 0, read 0, write 0, timeout 186
Requests/sec:    136.55
Transfer/sec:     47.07KB

wrk -r10000 -t5 -c50 "http://X.X.X.22:8888/"
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   239.44ms  410.80ms   3.59s    94.88%
    Req/Sec     0.00      0.00     0.00    100.00%
  10001 requests in 1.24m, 3.37MB read
  Socket errors: connect 0, read 0, write 0, timeout 17
Requests/sec:    134.01
Transfer/sec:     46.20KB


#-------------------------------------------------------
# Tornado_virtuoso 
<code>
import json
import urllib
import uuid
import tornado
from tornado import gen
from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import url_concat
import redis

from settings import SPARQL_ENDPOINT
from queries import GET_QUERY, POST_QUERY, DELETE_QUERY


class RootHandler(RequestHandler):

    SUPPORTED_METHODS = ("GET", "POST", "DELETE")

    @asynchronous
    @gen.engine
    def get(self):
        url = url_concat(SPARQL_ENDPOINT, {
            "query": GET_QUERY,
            "format": "application/sparql-results+json"
        })

        sparql_endpoint = self._get_async_client()

        response = yield gen.Task(sparql_endpoint.fetch, url)
        self.return_pretty_response_json(response)

    @asynchronous
    def post(self):
        # Passing a UUID to the uri to insert into the triplestore
        # So bechmark tests may want to insert X triplestore
        # Delete them all
        # Get them all
        # and so on
        self.modify_query(POST_QUERY % str(uuid.uuid4()))

    @asynchronous
    def delete(self):
        self.modify_query(DELETE_QUERY)

    @gen.engine
    def modify_query(self, query):
        body_encoded = urllib.urlencode({"query": query})
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/sparql-results+json",
            "format": "application/sparql-results+json"
        }

        request = HTTPRequest(url=SPARQL_ENDPOINT,
                              method="POST",
                              headers=headers,
                              body=body_encoded)
        sparql_endpoint = self._get_async_client()
        response = yield gen.Task(sparql_endpoint.fetch, request)
        self.return_pretty_response_json(response)

    def _get_async_client(self):
        AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        return AsyncHTTPClient()

    def return_pretty_response_json(self, response):
        result_dict = json.loads(response.body)
        pretty_json_string = json.dumps(result_dict, sort_keys=True, indent=4, separators=(",", ":"))
        self.finish(pretty_json_string)


class RedisHandler(RequestHandler):

    def initialize(self):
        self.redis_client = brukva.Client(host="localhost",
                                          port=6379,
                                          io_loop=tornado.ioloop.IOLoop.instance())

        self.redis_client = redis.Redis(host="localhost", port=6379)
        self.redis_client.connect()

    SUPPORTED_METHODS = ("GET", "POST", "DELETE")

    @asynchronous
    def get(self):
        self.redis_client.get("foo", self.on_result)

    @asynchronous
    def post(self):
        self.redis_client.set("foo", "bar", self.on_result)

    @asynchronous
    def delete(self):
        self.redis_client.delete("foo", self.on_result)

    def on_result(self, result):
        self.finish(str(result))

# Yeah, i know there is duplicated code. sue me!
# TODO refactor


class SyncronousRedisHandler(RequestHandler):

    def initialize(self):
        self.redis_client = redis.Redis(host="localhost",
                                        port=6379)

    SUPPORTED_METHODS = ("GET", "POST", "DELETE")

    @asynchronous
    def get(self):
        result = self.redis_client.get("foo")
        self.finish(str(result))

    @asynchronous
    def post(self):
        result = self.redis_client.set("foo", "bar")
        self.finish(str(result))

    @asynchronous
    def delete(self):
        result = self.redis_client.delete("foo")
        self.finish(str(result))


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", RootHandler),
            (r"/redis_async", RedisHandler),
            (r"/redis", SyncronousRedisHandler)
        ]
        super(Application, self).__init__(handlers)


if __name__ == "__main__":
    Application().listen(8888)
    print "The tornado is here..."
    tornado.ioloop.IOLoop.instance().start()
</code>

wrk -r1000 -t2 -c5 http://X.X.X.22:8888/
Making 1000 requests to http://X.X.X.22:8888/
  2 threads and 5 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.72ms    4.76ms  24.35ms   77.78%
    Req/Sec     0.00      0.00     0.00    100.00%
  1000 requests in 2.65s, 498.05KB read
Requests/sec:    377.55
Transfer/sec:    188.04KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    67.93ms   18.07ms 257.39ms   89.36%
    Req/Sec     0.00      0.00     0.00    100.00%
  10001 requests in 13.56s, 4.86MB read
Requests/sec:    737.40
Transfer/sec:    367.26KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.06ms   12.41ms 142.40ms   83.37%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 13.51s, 4.86MB read
Requests/sec:    740.14
Transfer/sec:    368.63KB

wrk -r10000 -t5 -c50 http://X.X.X.22:8888/
Making 10000 requests to http://X.X.X.22:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    68.96ms   29.06ms 423.30ms   95.68%
    Req/Sec     0.00      0.00     0.00    100.00%
  10002 requests in 13.93s, 4.86MB read
Requests/sec:    717.77
Transfer/sec:    357.48KB

#-------------------------------------------------------
# Tornado_virtuoso na Amazon Srv3

./wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    55.19ms    7.21ms  83.58ms   81.22%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 11.13s, 4.85MB read
Requests/sec:    898.11
Transfer/sec:    446.42KB

./wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    54.70ms    7.29ms  88.90ms   88.52%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 11.15s, 4.85MB read
Requests/sec:    896.87
Transfer/sec:    445.81KB

./wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    56.03ms    8.35ms  80.86ms   87.40%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 11.34s, 4.85MB read
Requests/sec:    881.46
Transfer/sec:    438.15KB

#-------------------------------------------------------
# Gevent_virtuoso sem print na Amazon Srv3

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   115.05ms   13.69ms 159.72ms   82.92%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 23.32s, 3.36MB read
Requests/sec:    428.79
Transfer/sec:    147.40KB

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   114.73ms   13.86ms 151.87ms   81.70%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 23.28s, 3.36MB read
Requests/sec:    429.61
Transfer/sec:    147.68KB

#-------------------------------------------------------
# Gevent_virtuoso_2 sem print na Amazon Srv3

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    94.60ms    6.28ms 127.64ms   98.74%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 19.08s, 3.36MB read
Requests/sec:    524.08
Transfer/sec:    180.15KB

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    94.71ms    3.59ms 103.70ms   91.77%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 19.08s, 3.36MB read
Requests/sec:    524.20
Transfer/sec:    180.19KB

#-------------------------------------------------------
# Gevent_pure_wsgi na Amazon Srv3

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.39ms    1.76ms  16.28ms   79.78%
    Req/Sec    22.47    149.05     1.00k    97.75%
  10000 requests in 2.74s, 1.56MB read
Requests/sec:   3644.92

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    14.21ms    0.88ms  17.96ms   79.80%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 2.94s, 1.56MB read
Requests/sec:   3404.44
Transfer/sec:    545.24KB

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.55ms    1.84ms  15.04ms   53.66%
    Req/Sec     0.00      0.00     0.00    100.00%
  10000 requests in 2.56s, 1.56MB read
Requests/sec:   3906.90
Transfer/sec:    625.71KB

#-------------------------------------------------------
# Tornado_sock na Amazon Srv3

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.48ms   46.74ms 219.66ms   95.35%
    Req/Sec   558.14    665.56     2.00k    90.70%
  10000 requests in 1.74s, 439.45KB read
Requests/sec:   5731.39
Transfer/sec:    251.87KB

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   447.40us  484.46us   1.38ms   79.07%
    Req/Sec   720.93    734.38     2.00k    83.72%
  10000 requests in 1.75s, 439.45KB read
Requests/sec:   5716.09
Transfer/sec:    251.20KB

#-------------------------------------------------------
# Gevent_sock na Amazon Srv3
wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.15ms  338.16us   7.74ms   75.51%
    Req/Sec     1.00k     0.00     1.00k   100.00%
  10000 requests in 1.51s, 439.45KB read
Requests/sec:   6617.00
Transfer/sec:    290.79KB

wrk -r10000 -t5 -c50 "http://Srv3:8888/"
Making 10000 requests to http://Srv3:8888/
  5 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.23ms  388.84us   8.24ms   71.70%
    Req/Sec     1.00k     0.00     1.00k   100.00%
  10000 requests in 1.52s, 439.45KB read
Requests/sec:   6577.87
Transfer/sec:    289.07KB

#-------------------------------------------------------
# Gevent_virtuoso2 na Amazon Srv3

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" http://Srv3:8888/
finished in 19 sec, 28 millisec and 232 microsec, 525 req/s, 180 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" http://Srv3:8888/
finished in 19 sec, 377 millisec and 764 microsec, 516 req/s, 177 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

#-------------------------------------------------------
# Gevent_virtuoso na Amazon Srv3

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" http://Srv3:8888/
finished in 22 sec, 232 millisec and 335 microsec, 449 req/s, 154 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" http://Srv3:8888/
finished in 22 sec, 676 millisec and 538 microsec, 440 req/s, 151 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

# Tornado_server na Amazon Srv3
weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" http://Srv3:8888/
finished in 10 sec, 864 millisec and 227 microsec, 920 req/s, 457 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

finished in 11 sec, 29 millisec and 829 microsec, 906 req/s, 450 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

#-------------------------------------------------------
# Gevent 1 server na Amazon Srv1 com banco em Srv2

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 24 sec, 307 millisec and 276 microsec, 411 req/s, 141 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 23 sec, 944 millisec and 71 microsec, 417 req/s, 143 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data


#-------------------------------------------------------
# Gevent 2 server na Amazon Srv1 com banco em Srv2

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 60 sec, 636 millisec and 298 microsec, 164 req/s, 56 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 58 sec, 241 millisec and 300 microsec, 171 req/s, 59 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

#-------------------------------------------------------
# Tornado server na Amazon Srv1 com banco em Srv2

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 10 sec, 89 millisec and 421 microsec, 991 req/s, 492 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 10 sec, 188 millisec and 275 microsec, 981 req/s, 487 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

#-------------------------------------------------------
# Tornado server sem CURL na Amazon Srv1 com banco em Srv2

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 15 sec, 896 millisec and 303 microsec, 629 req/s, 312 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 16 sec, 116 millisec and 627 microsec, 620 req/s, 308 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data


#-------------------------------------------------------
# Testes com Redis

#-------------------------------------------------------
Testes com conexões incrementais

./inc_test.sh  
<code>
#!/bin/bash
for i in 10 20 30 40 50
do
    echo "Conexoes $i"
    weighttp -n 10000 -c $i -t 10 -k -H "User-Agent: tati" http://Srv3:8888/
done
</code>

Executando com python servers/tornado_server.py

Conexoes 10
weighttp - a lightweight and simple webserver benchmarking tool
finished in 11 sec, 153 millisec and 877 microsec, 896 req/s, 445 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

Conexoes 20
weighttp - a lightweight and simple webserver benchmarking tool
finished in 11 sec, 122 millisec and 544 microsec, 899 req/s, 446 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

Conexoes 30
weighttp - a lightweight and simple webserver benchmarking tool
finished in 11 sec, 363 millisec and 772 microsec, 879 req/s, 437 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

Conexoes 40
weighttp - a lightweight and simple webserver benchmarking tool
finished in 11 sec, 589 millisec and 41 microsec, 862 req/s, 428 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

Conexoes 50
weighttp - a lightweight and simple webserver benchmarking tool
finished in 11 sec, 728 millisec and 529 microsec, 852 req/s, 423 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

#-------------------------------------------------------
# Executando com python servers/gevent_virtuoso.py

Conexoes 10
weighttp - a lightweight and simple webserver benchmarking tool
finished in 21 sec, 624 millisec and 868 microsec, 462 req/s, 158 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

Conexoes 20
weighttp - a lightweight and simple webserver benchmarking tool
finished in 22 sec, 373 millisec and 816 microsec, 446 req/s, 153 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

Conexoes 30
weighttp - a lightweight and simple webserver benchmarking tool
finished in 22 sec, 847 millisec and 966 microsec, 437 req/s, 150 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

Conexoes 40
weighttp - a lightweight and simple webserver benchmarking tool
finished in 32 sec, 440 millisec and 792 microsec, 308 req/s, 110 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 8652 succeeded, 1348 failed, 0 errored
status codes: 8652 2xx, 0 3xx, 0 4xx, 1348 5xx
traffic: 3669628 bytes total, 2077660 bytes http, 1591968 bytes data

Conexoes 50
weighttp - a lightweight and simple webserver benchmarking tool
finished in 38 sec, 940 millisec and 533 microsec, 256 req/s, 94 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 7909 succeeded, 2091 failed, 0 errored
status codes: 7909 2xx, 0 3xx, 0 4xx, 2091 5xx
traffic: 3752101 bytes total, 2296845 bytes http, 1455256 bytes data

#-------------------------------------------------------
Executando com python servers/gevent_virtuoso_2.py

Conexoes 10
weighttp - a lightweight and simple webserver benchmarking tool
finished in 19 sec, 276 millisec and 366 microsec, 518 req/s, 178 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

Conexoes 20
finished in 19 sec, 652 millisec and 699 microsec, 508 req/s, 174 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 3520000 bytes total, 1680000 bytes http, 1840000 bytes data

Conexoes 30
finished in 24 sec, 156 millisec and 234 microsec, 413 req/s, 143 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 9757 succeeded, 243 failed, 0 errored
status codes: 9757 2xx, 0 3xx, 0 4xx, 243 5xx
traffic: 3546973 bytes total, 1751685 bytes http, 1795288 bytes data

Conexoes 40
finished in 32 sec, 193 millisec and 224 microsec, 310 req/s, 110 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 8865 succeeded, 1135 failed, 0 errored
status codes: 8865 2xx, 0 3xx, 0 4xx, 1135 5xx
traffic: 3645985 bytes total, 2014825 bytes http, 1631160 bytes data

Conexoes 50
finished in 32 sec, 136 millisec and 842 microsec, 311 req/s, 110 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 8894 succeeded, 1106 failed, 0 errored
status codes: 8894 2xx, 0 3xx, 0 4xx, 1106 5xx
traffic: 3642766 bytes total, 2006270 bytes http, 1636496 bytes data


#==============================================================
# Testes com Pypy

#-------------------------------------------------------
# Tornado server na Amazon Srv1 com banco em Srv2

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 12 sec, 668 millisec and 910 microsec, 789 req/s, 392 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data

weighttp -n 10000 -c 20 -t 10 -k -H "User-Agent: tati" Srv1:8888
finished in 11 sec, 688 millisec and 195 microsec, 855 req/s, 425 kbyte/s
requests: 10000 total, 10000 started, 10000 done, 10000 succeeded, 0 failed, 0 errored
status codes: 10000 2xx, 0 3xx, 0 4xx, 0 5xx
traffic: 5090000 bytes total, 1590000 bytes http, 3500000 bytes data
