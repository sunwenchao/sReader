# -*- coding: utf-8 -*-
from os import path

dirname = path.dirname

ROOT_PATH = path.abspath(dirname(dirname(dirname(dirname(__file__)))))

# http server config
serverSettings = {
    'login_url': '/login',
    'static_path': path.join(ROOT_PATH, 'client'),
    'static_url_prefix': '/s/'
}


# jinja2 template config
from jinja2 import Environment, PackageLoader

TMPLATE_PACKAGE = 'views'

jinja_env = Environment(loader=PackageLoader(TMPLATE_PACKAGE, ''))