from decouple import config
from dj_database_url import parse as db_url
from unipath import Path


# Basic (self-explanatory) definitions
BASE_DIR = Path(__file__).ancestor(2)
DEBUG = config('DEBUG', default=True, cast=bool)


# Active apps
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # Third-party apps
    'compressor',

    # Local apps
    'backend.core.apps.DefaultApp',
]


# Active middlewares

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Third-party middlewares
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Local middlewares
]


# URL and gateway config
ROOT_URLCONF = 'backend.urls'
SITE_ID = 1
WSGI_APPLICATION = 'backend.wsgi.application'


# Database
DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///{}'.format(BASE_DIR.child('db.sqlite3')),
        cast=db_url),
}


# Internationalization
LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')
TIME_ZONE = config('TIME_ZONE', default='America/Fortaleza')
USE_I18N = True
USE_L10N = True
USE_TZ = True
