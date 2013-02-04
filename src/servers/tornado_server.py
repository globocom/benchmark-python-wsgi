import json
import tornado
from tornado import gen
from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import AsyncHTTPClient
from tornado.httputil import url_concat
from settings import SPARQL_ENDPOINT


class RootHandler(RequestHandler):

    #SUPPORTED_METHODS = ("GET", "POST")

    @asynchronous
    @gen.engine
    def get(self):
        query = "select distinct ?class where {?class a owl:Class} LIMIT 100"
        url = url_concat(SPARQL_ENDPOINT, {
            "query": query,
            "Accept": "application/sparql-results+json",
            "format": "application/sparql-results+json"
        })

        AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        sparql_endpoint = AsyncHTTPClient()

        response = yield gen.Task(sparql_endpoint.fetch, url)
        result_dict = json.loads(response.body)
        pretty_json_string = json.dumps(result_dict, sort_keys=True, indent=4, separators=(",", ":"))
        self.write(pretty_json_string)
        self.flush()

    def post(self):
        pass


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", RootHandler)
        ]
        super(Application, self).__init__(handlers)
        # TODO db connection


if __name__ == "__main__":
    Application().listen(8888)
    print "The tornado is here..."
    tornado.ioloop.IOLoop.instance().start()
