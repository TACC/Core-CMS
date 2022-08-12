"""Configure email settings (for apps e.g. djangocms_forms)"""

########################
# DJANGO
########################

# Development
# https://docs.djangoproject.com/en/2.1/topics/email/#configuring-email-for-development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = 'no-reply@localhost'

# Production
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '?'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = '?'
# EMAIL_HOST_PASSWORD = '?'
# DEFAULT_FROM_EMAIL = 'no-reply@...'
