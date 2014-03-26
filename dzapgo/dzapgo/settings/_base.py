"""
Django settings for dzapgo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJ_DIR = os.path.abspath(os.path.join(BASE_DIR, '../'))

sys.path.insert(0, os.path.join(PROJ_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^gx18ajg3civ2=kn6gqorqzn8(+zql-9u^!2e1^s19t21u^91-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_hooks',
    'notes',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dzapgo.urls'

WSGI_APPLICATION = 'dzapgo.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(PROJ_DIR, 'templates')),
    )

# STATICFILES_DIRS = (
#     os.path.abspath(os.path.join(PROJ_DIR, 'static')),
#     )

# Database/PostgreSQL settings

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'zapier',
        'USER': 'zapier',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Webhooks 
HOOK_EVENTS = {
    'note.updated': 'notes.Note.updated',
    'note.viewed': None
}
HOOK_DELIVERER = 'notes.tasks.deliver_hook_wrapper'

# Celery broker 
BROKER_URL = 'redis://localhost:6379'