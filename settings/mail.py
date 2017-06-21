from decouple import config

# E-mail configuration
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')
EMAIL_BACKEND = config(
    'EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend'
)
EMAIL_HOST = config('EMAIL_HOST', default='smtp.sendgrid.net')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD', default='')
EMAIL_HOST_USER = config('SENDGRID_USERNAME', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
