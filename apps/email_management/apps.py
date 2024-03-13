from django.apps import AppConfig
import logging
import requests
from djangocms_forms.signals import form_submission
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(f"portal.{__name__}")
service_url = settings.TUP_SERVICES_URL
if settings.DEBUG:
    service_url = service_url.replace("localhost", "host.docker.internal")


QUEUE_MAP = {
    "Allocations": "Allocations",
    "Login Issues": "Accounts",
    "Multi-factor Authentication": "MFA",
    "Data Analytics or Storage Resources": "Data Intensive Computing",
    "Login/Authentication Issue": "Accounting",
    "Running Jobs or Using TACC Resources": "High Performance Computing",
    "Security Incident": "NSO",
    "Arecibo Data": "High Performance Computing",
    "Other": "High Performance Computing"
}


def submit_ticket(form_data):
    message_body = ""
    message_body += f"Category: {form_data['category']}\n"
    message_body += f"System/Resource: {form_data['systemresource']}\n"
    message_body += f"Requestor: {form_data['first-name']} {form_data['last-name']} ({form_data['email']})\n\n"
    message_body += form_data['message']

    ticket_data = {
        "email": form_data["email"],
        "subject": form_data["subject"],
        "description": message_body,
        "queue": QUEUE_MAP.get(form_data['category'], 'Accounting')
    }
    logger.debug(ticket_data)
    requests.post(f"{service_url}/tickets/noauth", data=ticket_data, files=[])


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
    [form_data["email"]],
    html_message=email_body)


def callback(form, cleaned_data, **kwargs):
    logger.debug(f"received submission from {form.name}")
    if form.name == 'rt-ticket-form':
        submit_ticket(cleaned_data)
    elif hasattr(cleaned_data, "email"):
        send_confirmation_email(form.name, cleaned_data)


class EmailManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_management'

    def ready(self):
        form_submission.connect(callback)