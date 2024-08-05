"""
Настоящие системы логирования очень распределенные и орудуют большим количеством связанных компонентов.
Давайте попробуем создать подобный механизм. Ваши настройки логирования должны выполнять следующее:

В консоль должны выводиться все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения.
Для сообщений WARNING и выше дополнительно должен выводиться путь к источнику события
(используется аргумент pathname в форматировании).
А для сообщений ERROR и CRITICAL еще должен выводить стэк ошибки (аргумент exc_info).
Сюда должны попадать все сообщения с основного логгера django.
В файл general.log должны выводиться сообщения уровня INFO и выше только с указанием времени,
уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение.
Сюда также попадают сообщения с регистратора django.
В файл errors.log должны выводиться сообщения только уровня ERROR и CRITICAL.
В сообщении указывается время, уровень логирования, само сообщение, путь к источнику сообщения и стэк ошибки.
В этот файл должны попадать сообщения только из логгеров django.request, django.server, django.template,
django.db.backends.
В файл security.log должны попадать только сообщения, связанные с безопасностью,
а значит только из логгера django.security. Формат вывода предполагает время, уровень логирования, модуль и сообщение.
На почту должны отправляться сообщения уровней ERROR и выше из django.request и django.server по формату,
как в errors.log, но без стэка ошибок.
Более того, при помощи фильтров нужно указать, что в консоль сообщения отправляются только при DEBUG = True,
а на почту и в файл general.log — только при DEBUG = False.
"""

import logging
import logging.config
from django.utils.log import AdminEmailHandler

DEBUG = False  # Установить True для локальной разработки

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
        },
        'console_with_path': {
            'format': '[%(asctime)s] %(levelname)s: %(pathname)s - %(message)s',
        },
        'console_with_stack': {
            'format': '[%(asctime)s] %(levelname)s: %(pathname)s - %(message)s\n%(exc_info)s',
        },
        'file': {
            'format': '[%(asctime)s] %(levelname)s: %(module)s - %(message)s',
        },
        'file_with_stack': {
            'format': '[%(asctime)s] %(levelname)s: %(pathname)s - %(message)s\n%(exc_info)s',
        },
        'security': {
            'format': '[%(asctime)s] %(levelname)s: %(module)s - %(message)s',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'console_with_path': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_with_path',
        },
        'console_with_stack': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_with_stack',
        },
        'file_general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'file',
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'file_with_stack',
        },
        'file_security': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'security',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'file_with_stack',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_with_path', 'console_with_stack', 'file_general'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
