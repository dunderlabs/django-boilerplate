from .base import env

# E-mail configuration
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL', '')
EMAIL_BACKEND = env.str(
    'EMAIL_BACKEND',
    'django.core.mail.backends.smtp.EmailBackend',
)
EMAIL_HOST = env.str('EMAIL_HOST', 'smtp.sendgrid.net')
EMAIL_HOST_PASSWORD = env.str('SENDGRID_PASSWORD', '')
EMAIL_HOST_USER = env.str('SENDGRID_USERNAME', '')
EMAIL_PORT = env.int('EMAIL_PORT', 587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', True)
