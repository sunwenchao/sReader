# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import memcache

from config import routing
from config import server
from session import mcsession
from utils import database

class Application(tornado.web.Application):
    def __init__(self):

        handlers = routing.routingList
        settings = server.serverSettings

        tornado.web.Application.__init__(self, handlers, **settings)

        self.session_db_con = memcache.Client(server.sessionAddrs, debug=0)

        self.session_store = mcsession.MCSessionStore(self.session_db_con, **server.sessionManagerOpt)


def init():

    database.create_db()

    application = Application()

    application.listen(server.SERVER_PORT)
    tornado.ioloop.IOLoop.instance().start()