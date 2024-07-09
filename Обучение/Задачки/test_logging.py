import logging

# Получаем основного логгера Django
logger = logging.getLogger('django')
request_logger = logging.getLogger('django.request')
server_logger = logging.getLogger('django.server')
template_logger = logging.getLogger('django.template')
db_logger = logging.getLogger('django.db.backends')
security_logger = logging.getLogger('django.security')

def test_logging():
    logger.debug('This is a DEBUG message')
    logger.info('This is an INFO message')
    logger.warning('This is a WARNING message')
    logger.error('This is an ERROR message', exc_info=True)
    logger.critical('This is a CRITICAL message', exc_info=True)

    request_logger.error('This is a request ERROR message', exc_info=True)
    server_logger.error('This is a server ERROR message', exc_info=True)
    template_logger.error('This is a template ERROR message', exc_info=True)
    db_logger.error('This is a DB backends ERROR message', exc_info=True)
    security_logger.warning('This is a security WARNING message')

# Вызов тестовой функции
test_logging()
