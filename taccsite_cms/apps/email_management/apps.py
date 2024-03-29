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

    def replace_word_in_file(file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()

        modified_content = file_content.replace('{site_name}', f'{site_name}')
        return modified_content

    text_file = "taccsite_cms/apps/email_management/assets/confirmation_email.txt"
    html_file = "taccsite_cms/apps/email_management/assets/confirmation_email.html"

    text_body = replace_word_in_file(text_file)
    email_body = replace_word_in_file(html_file)

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
    name = 'common_apps.email_management'

    def ready(self):
        form_submission.connect(callback)
