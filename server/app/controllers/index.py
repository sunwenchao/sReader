# -*- coding: utf-8 -*-
import tornado
from controllers import base_handler

class MainHandler(base_handler.BaseHandler):

    @tornado.web.authenticated
    def get(self):

        self.write('123')