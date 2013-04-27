# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from config import routing
from config import server

application = tornado.web.Application(routing.routingList, **server.serverSettings)

def init():
    application.listen(server.SERVER_PORT)
    tornado.ioloop.IOLoop.instance().start()