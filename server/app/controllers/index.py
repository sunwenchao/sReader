# -*- coding: utf-8 -*-

import tornado.web
from config import environment

class MainHandler(tornado.web.RequestHandler):

    @tornado.web.authenticated
    def get(self):

        self.write('123')