import tornado
from tornado.web import RequestHandler

class RootHandler(RequestHandler):

    #SUPPORTED_METHODS = ("GET", "POST")

    def get(self):
        self.write("WORKING")

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
