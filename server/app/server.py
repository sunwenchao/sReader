# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from config import routing
from config import environment

application = tornado.web.Application(routing.routingList, **environment.serverSettings)

def init():
    application.listen(9000)
    tornado.ioloop.IOLoop.instance().start()