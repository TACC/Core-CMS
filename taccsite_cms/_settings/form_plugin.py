"""Configure djangocms_forms and related apps"""

from django.utils.translation import gettext_lazy as _

########################
# KNOWN ISSUES
########################

# Unable to export to Excel nor YAML
# (No success hiding those formats from editor)
# https://github.com/avryhof/djangocms-forms/issues/8

########################
# DJANGOCMS_FORMS
# https://github.com/avryhof/djangocms-forms/
########################

# DJANGOCMS_FORMS_PLUGIN_MODULE = ('Generic')
# DJANGOCMS_FORMS_PLUGIN_NAME = ('Form')

# DJANGOCMS_FORMS_TEMPLATES = (
#     ('djangocms_forms/form_template/default.html', ('Default')),
# )
DJANGOCMS_FORMS_USE_HTML5_REQUIRED = True

# DJANGOCMS_FORMS_REDIRECT_DELAY = 1000

# The default value is only for test and dev
# DJANGO_FORMS_RECAPTCHA_PUBLIC_KEY = ''
# DJANGO_FORMS_RECAPTCHA_SECRET_KEY = ''

DJANGOCMS_FORMS_SPAM_PROTECTIONS = (
    (0, _('None')),
    # (1, _('Honeypot')), # if necessary, learn how to use
    (2, _('ReCAPTCHA')),
)
DEFAULT_SPAM_PROTECTION = 0

# Improve form legibility and conceal broken features
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
            'description': 'Whether to save form data.',
            'fields': (
                'save_data',
            ),
        },
    ),
    (
        _('Submission settings (unavailable features)'),
        {
            'classes': ('collapse',),
            'description': 'Choose storage options to capture form data. You can enter an e-mail address to which to e-mail form submissions.',
            'fields': (
                # Submitting form with 'email_to' defined causes server error
                # FAQ: We may need to setup some django e-mail server for these
                'email_to',
                'email_from',
                'email_subject',
                'email_uploaded_files',
                # Uncertain whether this works
                # FAQ: It may not work only cuz of general form submission error
                'spam_protection',
            ),
        },
    ),
)

########################
# DJANGO
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
