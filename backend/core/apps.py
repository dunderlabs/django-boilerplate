from django.apps import AppConfig
from settings.base import BASE_DIR


class DefaultApp(AppConfig):
    label = 'core'
    name = 'backend.core'
    path = BASE_DIR.child('backend', 'core')
    verbose_name = 'Core Application'
