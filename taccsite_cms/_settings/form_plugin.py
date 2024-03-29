"""Configure djangocms_forms and related apps"""

from django.utils.translation import gettext_lazy as _

########################
# DJANGO_RECAPTCHA
# https://github.com/avryhof/django-recaptcha/
########################

# To properly avoid client error about using test keys,
# define RECAPTCHA_..._KEY settings on client-facing servers

########################
# DJANGOCMS_FORMS
# https://github.com/TACC/djangocms-forms/
########################

DJANGOCMS_FORMS_USE_HTML5_REQUIRED = True

DJANGOCMS_FORMS_SPAM_PROTECTIONS = (
    (0, _('None')),
    # (1, _('Honeypot')), # if necessary, learn how to use
    (2, _('ReCAPTCHA')),
)
DEFAULT_SPAM_PROTECTION = 0

# Improve form legibility and conceal unavailable features
# https://github.com/avryhof/djangocms-forms/blob/97d7c21/djangocms_forms/cms_plugins.py#L69-L121
DJANGOCMS_FORMS_FIELDSETS = (
    (None, {'fields': ('name', 'form_template',),}),
    (
        _('Text'),
        {
            'description': _(
                'The <strong>Title</strong> and <strong>Description</strong> '
                'will display above the input fields and Submit button.'
            ),
            'fields': ('title', 'description','submit_btn_txt',),
        },
    ),
    (
        None,
        {
            'description': _(
                'You can change the message that appears <em>after</em> someone submits your form. By default, this says "<strong>Thank you!</strong>"'
            ),
            'fields': ('post_submit_msg',),
        },
    ),
    (
        _('Redirect settings'),
        {
            'description': _(
                'Whether and how to redirect the form <em>after</em> submission.'
            ),
            'fields': ('success_redirect', ('page_redirect', 'external_redirect'), 'redirect_delay',),
        }
    ),
    (
        _('Submission settings'),
        {
            'description': 'You can choose to set from which, and to which, e-mail address to send form submissions and/or to save submitted form data in the CMS database. <small>The CMS default <em>from</em> address (<code>DEFAULT_FROM_EMAIL</code>) will be used if "SENDER EMAIL ADDRESS" is blank.</small>',
            'fields': (
                'email_to',
                'email_from',
                'email_subject',
                # 'email_uploaded_files', # file upload not yet supported
                'save_data',
                'spam_protection',
            ),
        },
    ),
)

DJANGOCMS_FORMS_FORMAT_CHOICES = (
    ("csv", _("CSV")),
    ("json", _("JSON")),
)

########################
# DJANGO: FORM
# https://docs.djangoproject.com/en/2.2/ref/settings/#form-renderer
########################

# Allow form template override
# https://github.com/torchbox/django-recaptcha/issues/211#issuecomment-675608391
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

########################
# DJANGO CMS
########################

_INSTALLED_APPS = [
    'djangocms_forms',         # form plugin for editors
    'django.forms',            # support form template override
    'captcha',                 # support recaptcha for djangocms_forms
]
