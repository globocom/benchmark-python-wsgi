import json
import urllib
import uuid
import tornado
from tornado import gen
from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import url_concat
import brukva

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

        request =   HTTPRequest(url=SPARQL_ENDPOINT,
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


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", RootHandler),
            (r"/redis", RedisHandler)
        ]
        super(Application, self).__init__(handlers)


if __name__ == "__main__":
    Application().listen(8888)
    print "The tornado is here..."
    tornado.ioloop.IOLoop.instance().start()
