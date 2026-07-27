"""Configure email settings (for apps e.g. djangocms_forms)"""

########################
# DJANGO: EMAIL
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

########################
# TACC: EMAIL
########################

PORTAL_SHOULD_SEND_CONF_EMAIL = False

PORTAL_CONF_EMAIL_TEXT = """
Greetings,

You have successfully submitted a form on the {site_name} website. Thank you for your submission.

Sincerely,
{site_name} Communications
"""

PORTAL_CONF_EMAIL_HTML = """
<p>Greetings,</p>
<p>
  You have successfully submitted a form on the {site_name} website. Thank you
  for your submission.
</p>
<p>
  Sincerely,<br />
  {site_name} Communications
</p>
"""
