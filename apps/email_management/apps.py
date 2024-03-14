from django.apps import AppConfig
import logging
from djangocms_forms.signals import form_submission
from django.core.mail import send_mail

logger = logging.getLogger(f"portal.{__name__}")

def send_confirmation_email(form_name, form_data):

    email_body = """
            <p>Greetings,</p>
            <p>
                Your have successfully submitted a form on the TACC website. Thank you for your submission.
            </p>
            <p>
                Business hours are Monday - Friday, 8AM to 5PM Central. We will respond to your submission
                according to the information provided on the form webpage.
            </p>
            <p>
            Sincerely,<br>
            TACC Communications
            </p>
            """
    send_mail(
    f"TACC Form Submission Received: {form_name}",
    email_body,
    "no-reply@tacc.utexas.edu",
    [form_data['email']],
    html_message=email_body)


def callback(form, cleaned_data, **kwargs):
    logger.debug(f"received submission from {form.name}")
    logger.debug(type(cleaned_data))
    if ('email' in cleaned_data):
        send_confirmation_email(form.name, cleaned_data)

class EmailManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.email_management'

    def ready(self):
        form_submission.connect(callback)