# Django settings for {{ project_name }} project.
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Admin', 'admin@scopart.fr'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{project_name}}',
        'USER': '{{project_name}}',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1',]
TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PACKAGE_ROOT, 'site_media', 'media')
MEDIA_URL = '/site_media/media/'

STATIC_ROOT = os.path.join(PACKAGE_ROOT, 'site_media', 'static')
STATIC_URL = '/site_media/static/'
STATICFILES_DIRS = (
    os.path.join(PACKAGE_ROOT, "static"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '{{ secret_key }}'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '{{project_name}}.urls'

WSGI_APPLICATION = '{{project_name}}.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PACKAGE_ROOT, "templates"),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
