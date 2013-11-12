from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.sqlite',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
