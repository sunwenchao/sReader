# -*- coding: utf-8 -*-
import logging
import config.environment as env

LOGGING_FORMAT = '[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s'
DATE_FORMAT = '%y-%m-%d %H:%M:%S'

logging_level = logging.DEBUG if env.DEBUG_MODE else logging.ERROR

logging.basicConfig(
    level=logging_level,
    format=LOGGING_FORMAT,
    datefmt=DATE_FORMAT
)

defaultLogger = logging.getLogger('sreader')


# exc_info=True to have stack
def getLogger():
    return defaultLogger
