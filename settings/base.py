from unipath import Path

from dj_database_url import parse as db_url
from environs import Env


env = Env()
env.read_env()  # read .env file, if it exists


# Basic (self-explanatory) definitions
BASE_DIR = Path(__file__).ancestor(2)
DEBUG = env.bool('DEBUG', True)


# Active apps
DJANGO_APPS = [
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
]

LOCAL_APPS = [
    'backend.core.apps.DefaultApp',
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


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
    'default': env.dj_db_url(
        'DATABASE_URL',
        'sqlite:///{}'.format(BASE_DIR.child('db.sqlite3')),
    ),
}


# Internationalization
LANGUAGE_CODE = env.str('LANGUAGE_CODE', 'en-us')
TIME_ZONE = env.str('TIME_ZONE', 'America/Fortaleza')
USE_I18N = True
USE_L10N = True
USE_TZ = True
