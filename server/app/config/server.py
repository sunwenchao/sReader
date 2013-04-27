# -*- coding: utf-8 -*-
from os import path
from environment import ROOT_PATH

SERVER_PORT = '9000'

# http server config
serverSettings = {
    'login_url': '/login',
    'static_path': path.join(ROOT_PATH, 'client'),
    'static_url_prefix': '/s/'
}
