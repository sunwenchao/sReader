# -*- coding: utf-8 -*-
from os import path
from environment import ROOT_PATH

SERVER_PORT = '9000'

# http server config
serverSettings = {
    'login_url': '/login',
    'static_path': path.join(ROOT_PATH, 'client'),
    'static_url_prefix': '/s/',
    'cookie_secret': 'sun'
}

# server session config
sessionAddrs = ['127.0.0.1:11211']

sessionManagerOpt = {
    'key_prefix': 'session',
    'expire': 30 * 24 * 60 * 60,
}
