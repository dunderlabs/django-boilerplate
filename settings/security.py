from .base import env


# Key for salting hashes and such
SECRET_KEY = env.str('SECRET_KEY', default='changeme')

# Host names allowed when DEBUG=False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', ['*'])
