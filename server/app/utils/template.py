# -*- coding: utf-8 -*-

# jinja2 template config
from jinja2 import Environment, PackageLoader

TMPLATE_PACKAGE = 'views'

jinja_env = Environment(loader=PackageLoader(TMPLATE_PACKAGE, ''))