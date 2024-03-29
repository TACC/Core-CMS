from django.apps import AppConfig
import logging
from djangocms_forms.signals import form_submission
from django.core.mail import send_mail
from django.conf import settings

PORTAL_SHOULD_SEND_CONF_EMAIL = settings.PORTAL_SHOULD_SEND_CONF_EMAIL

logger = logging.getLogger(f"portal.{__name__}")

def send_confirmation_email(form_name, form_data):

    from django.contrib.sites.models import Site

    # Get the current site
    current_site = Site.objects.get_current()

    # Get the site name
    site_name = current_site.name

    text_body = f"""
    Greetings,

    You have successfully submitted a form on the {site_name} website. Thank you for your submission.

    Sincerely,
    {site_name} Communications
    """
    email_body = f"""
    <p>Greetings,</p>
    <p>
    You have successfully submitted a form on the {site_name} website. Thank you for your submission.
    </p>
    <p>
    Sincerely,<br>
    {site_name} Communications
    </p>
    """
    send_mail(
    f"TACC Form Submission Received: {form_name}",
    text_body,
    "no-reply@tacc.utexas.edu",
    [form_data['email']],
    html_message=email_body)


def callback(form, cleaned_data, **kwargs):
    logger.debug(f"received submission from {form.name}")
    logger.debug(type(cleaned_data))
    if ('email' in cleaned_data and PORTAL_SHOULD_SEND_CONF_EMAIL):
        send_confirmation_email(form.name, cleaned_data)

class EmailManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.email_management'

    def ready(self):
        form_submission.connect(callback)