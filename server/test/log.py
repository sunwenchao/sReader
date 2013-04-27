import logging

logger = logging.getLogger()

# logger.level = logging.DEBUG

logger.handlers = []

logging.basicConfig(level=logging.DEBUG)

logger.debug('asdasd')
logger.info('asdasd')