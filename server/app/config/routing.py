# -*- coding: utf-8 -*-

from controllers import *

routingList = [

    (r"/", index.MainHandler),
    (r"/login", auth.LoginHandler)
]