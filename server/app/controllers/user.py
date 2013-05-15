# -*- coding: utf-8 -*-
from controllers import base_handler
from utils import database

class CheckNameHandler(base_handler.BaseHandler):

    def get(self):

        username_input = self.get_argument('username')

        db_session = database.getSession()
        r = db_session.execute('select * from user where username = "%s"' % (username_input, )).first()

        if r is None:
            self.send_json(code=self.DEFAULT_ERROR_CODE)
        else:
            self.send_json(code=self.DEFAULT_SUCCESS_CODE)

