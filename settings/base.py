from environs import Env
from unipath import Path

env = Env()
env.read_env()  # read .env file, if it exists


# Basic (self-explanatory) definitions
BASE_DIR = Path(__file__).ancestor(2)
DEBUG = env.bool("DEBUG", False)


# Active apps
DJANGO_APPS = [
    # Django built-in apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
]
LOCAL_APPS = [
    "backend.core.apps.DefaultApp",
]
THIRD_PARTY_APPS = [
    "compressor",
]


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


# Active middlewares

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Third-party middlewares
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Local middlewares
]


# URL and gateway config
ROOT_URLCONF = "backend.urls"
SITE_ID = 1
WSGI_APPLICATION = "backend.wsgi.application"


# Database
DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL",
        "sqlite:///{}".format(BASE_DIR.child("db.sqlite3")),
    ),
}


# Internationalization
LANGUAGE_CODE = env.str("LANGUAGE_CODE", "en-us")
TIME_ZONE = env.str("TIME_ZONE", "America/Fortaleza")
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ----------------------------
# Security                   |
# ----------------------------

# Key for salting hashes and such
SECRET_KEY = env.str("SECRET_KEY", default="changeme")

# Host names allowed when DEBUG=False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", ["*"])


# ----------------------------
# Static configuration       |
# ----------------------------


# URLs to serve media and static files
STATIC_URL = env.str("STATIC_URL", default="/static/")
MEDIA_URL = env.str("MEDIA_URL", default="/media/")

# Directories to save media and compiled static files
MEDIA_ROOT = BASE_DIR.child("_public", "media")
STATIC_ROOT = BASE_DIR.child("_public", "static")

# Directories to find static files
STATICFILES_DIRS = [
    BASE_DIR.child("frontend"),
    BASE_DIR.child("frontend", "bower_components"),
]

# Static files finding engines
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


# Pre-processing and compression
_bower = BASE_DIR.child("frontend", "bower_components")

_sass_includes = " ".join(
    [
        "--include-path={}".format(_bower.child("susy", "sass")),
    ]
)

COMPRESS_PRECOMPILERS = [
    ("text/x-scss", "pysassc {infile} {outfile} " + _sass_includes),
]

COMPRESS_CSS_FILTERS = [
    "compressor.filters.cssmin.rCSSMinFilter",
]

COMPRESS_JS_FILTERS = [
    "compressor.filters.jsmin.JSMinFilter",
]

# Template finders and processors
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR.child("frontend", "templates"),
        ],
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]


# ----------------------------
# E-mail configuration       |
# ----------------------------

DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", "")
EMAIL_BACKEND = env.str(
    "EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_HOST = env.str("EMAIL_HOST", "smtp.sendgrid.net")
EMAIL_HOST_PASSWORD = env.str("SENDGRID_PASSWORD", "")
EMAIL_HOST_USER = env.str("SENDGRID_USERNAME", "")
EMAIL_PORT = env.int("EMAIL_PORT", 587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", True)
