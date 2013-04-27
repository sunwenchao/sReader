# -*- coding: utf-8 -*-

import tornado.web
from config import environment

class LoginHandler(tornado.web.RequestHandler):

    def get(self):

        h = {'name': 'fish'}

        tpl = environment.jinja_env.get_template('login.html')

        self.write(tpl.render(h))