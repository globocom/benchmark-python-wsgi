from tornado.web import RequestHandler
import tornado.ioloop
import tornado.web


class RootHandler(RequestHandler):

    def get(self):
        self.write("WORKING")

    def post(self):
        pass

application = tornado.web.Application([
    (r"/", RootHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
