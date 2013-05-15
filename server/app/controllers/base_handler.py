# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
from utils.template import jinja_env
from session import mcsession

class BaseHandler(RequestHandler):

    DEFAULT_SUCCESS_CODE = 200
    DEFAULT_ERROR_CODE = 500

    def initialize(self):
        pass
        # self.db_session = database.getSession()

    def get_current_user(self):
        return self.session if self.session and 'username' in self.session else None

    @property
    def session(self):
        sessionid = self.get_secure_cookie('sid')
        return mcsession.Session(self.application.session_store, sessionid)

    def render_string(self, template_name, **kwargs):
        """Generate the given template with the given arguments.
            todo cache
        """
        tpl = jinja_env.get_template(template_name)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)

        return tpl.render(namespace)

    def send_json(self, code=DEFAULT_SUCCESS_CODE, data=None):
        r = {
            'code': code,
            'data': data
        }
        self.write(r)

    def on_finish(self):
        pass
        # self.db_session.close()
