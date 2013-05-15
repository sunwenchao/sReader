# -*- coding: utf-8 -*-

from controllers import *

routingList = [

    (r"/", index.MainHandler),
    (r"/login", auth.LoginHandler),
    (r"/reg", auth.RegHandler),
    (r"/user/checkname", user.CheckNameHandler)
]