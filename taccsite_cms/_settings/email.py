"""Configure email settings (for apps e.g. djangocms_forms)"""

########################
# DJANGO
# https://docs.djangoproject.com/en/2.2/topics/email/
########################

# Development, Staging, Production
# https://confluence.tacc.utexas.edu/x/coR9E
# !!!: Do NOT enable on a local computer!
#      Misue will trigger a security alert,
#      and your computer will be confiscated!
# EMAIL_HOST = "..."
# DEFAULT_FROM_EMAIL = 'no-reply@...' # where ... is project's production domain

# Debugging
# https://docs.djangoproject.com/en/2.1/topics/email/#configuring-email-for-development
# !!!: Do NOT enable on a local computer!
#      Misue will trigger a security alert,
#      and your computer will be confiscated!
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# DEFAULT_FROM_EMAIL = 'no-reply@localhost'
