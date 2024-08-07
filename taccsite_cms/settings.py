
"""
Django settings
Generated by 'django-admin startproject' using Django 1.11.22.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import logging
import os
from glob import glob

from django.utils.translation import gettext_lazy as _

from taccsite_cms._settings.auth import *
from taccsite_cms._settings.email import *
from taccsite_cms._settings.form_plugin import *
from taccsite_cms._settings.form_plugin import (
    _INSTALLED_APPS as form_plugin_INSTALLED_APPS
)

def gettext(s): return s

########################
# DJANGO
########################

SECRET_KEY = 'CHANGE_ME'


DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True       # False for Prod.

# Specify allowed hosts or use an asterisk to allow any host.
# ALLOWED_HOSTS = ['hostname.tacc.utexas.edu', 'client.org'] # Dev/Prod/Etc
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']   # Local

LOGOUT_REDIRECT_URL = '/'

# https://docs.djangoproject.com/en/3.0/ref/clickjacking/#how-to-use-it
X_FRAME_OPTIONS = 'SAMEORIGIN'

# whether the session cookie should be secure (https:// only)
SESSION_COOKIE_SECURE = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



########################
# STORAGE
########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'PORT': '5432',
        'NAME': 'taccsite',
        'USER': 'postgresadmin',
        'PASSWORD': 'taccforever',  # Change before live deployment.
        'HOST': 'core_cms_postgres'
    }
}



########################
# LOGGING
########################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[DJANGO] %(levelname)s %(asctime)s UTC %(module)s '
                      '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
        },
        'metrics': {
            'format': '[METRICS] %(levelname)s %(asctime)s UTC %(module)s '
                      '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/cms/cms.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
        'metrics_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'metrics',
        },
        'metrics_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/cms/metrics.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'metrics',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'portal': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'metrics': {
            'handlers': ['metrics_console', 'metrics_file'],
            'level': 'DEBUG',
        },
        'paramiko': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'celery': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'daphne': {
            'handlers': [
                'console',
            ],
            'level': 'INFO'
        }
    },
}

########################
# DJANGO_CMS
########################

SITE_ID = 1

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('guide.html', 'Guide'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),

    # TODO: WP-394: Retire deprecated page templates
    ('guides/getting_started.v3.html', 'Guide: Getting Started (v3)'),
    ('guides/getting_started.tam.html', 'Guide: Getting Started (TAM)'),
    ('guides/getting_started.v2.html', 'Guide: Getting Started (v2)'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
)

CMS_PERMISSION = True



########################
# TACC: GOOGLE ANALYTICS
########################

# To use during dev, Tracking Protection in browser needs to be turned OFF.
GOOGLE_ANALYTICS_PROPERTY_ID = "UA-123ABC@%$&-#"
GOOGLE_ANALYTICS_PRELOAD = True


########################
# TACC: BRANDING (DEPRECATED)
########################

# TACC_BRANDING = [
#     "tacc",                                  # (unused value)
#     "site_cms/img/org_logos/tacc-white.png", # "img_file_src"
#     "branding-tacc",                         # "img_class"
#     "https://www.tacc.utexas.edu/",          # "link_href"
#     "_blank",                                # "link_target"
#     "TACC Logo",                             # "img_alt_text"
#     "anonymous",                             # "img_crossorigin"
#     "True"                                   # (whether to show logo)
# ]
# UTEXAS_BRANDING = [
#     "utexas",                                    # (unused value)
#     "site_cms/img/org_logos/utaustin-white.png", # "img_file_src"
#     "branding-utaustin",                         # "img_class"
#     "https://www.utexas.edu/",                   # "link_href"
#     "_blank",                                    # "link_target"
#     "University of Texas at Austin Logo",        # "img_alt_text"
#     "anonymous",                                 # "img_crossorigin"
#     "True"                                       # (whether to show logo)
# ]
# NSF_BRANDING = [
#     "nsf",                                  # (unused value)
#     "site_cms/img/org_logos/nsf-white.png", # "img_file_src"
#     "branding-nsf",                         # "img_class"
#     "https://www.nsf.gov/",                 # "link_href"
#     "_blank",                               # "link_target"
#     "NSF Logo",                             # "img_alt_text"
#     "anonymous",                            # "img_crossorigin"
#     "True"                                  # (whether to show logo)
# ]

# To hide branding, add custom style `#header-branding { display: none; }`
# BRANDING = [ TACC_BRANDING, UTEXAS_BRANDING ]


########################
# TACC: BRANDING
########################

from taccsite_cms._settings.branding import *

# To hide branding, set `PORTAL_BRANDING = False`
PORTAL_BRANDING = [ PORTAL_BRANDING_TACC, PORTAL_BRANDING_UTEXAS ]


########################
# TACC: LOGO & FAVICON (DEPRECATED)
########################

# LOGO = [
#     "portal",                            # (unused value)
#     "site_cms/img/org_logos/portal.png", # "img_file_src"
#     "",                                  # "img_class"
#     "/",                                 # "link_href"
#     "_self",                             # "link_target"
#     "Portal Logo",                       # "img_alt_text"
#     "anonymous",                         # "img_crossorigin"
#     "True"                               # (whether to show logo)
# ]

# FAVICON = {
#     "img_file_src": "site_cms/img/favicons/favicon.ico",
#     "is_remote": False
# }


########################
# TACC: LOGO & FAVICON
########################

PORTAL_LOGO = {
    "is_remote": False,
    "img_file_src": "site_cms/img/org_logos/portal.png",
    "img_class": "", # additional class names
    "link_href": "/",
    "link_target": "_self",
    "img_alt_text": "Portal Logo",
    "img_crossorigin": "anonymous",
} # To hide logo, set `PORTAL_LOGO = False`

PORTAL_FAVICON = {
    "is_remote": False,
    "img_file_src": "site_cms/img/favicons/favicon.ico",
}


########################
# TACC: PORTAL
########################

PORTAL_IS_TACC_CORE_PORTAL = True
PORTAL_HAS_LOGIN = True
PORTAL_HAS_SEARCH = True

# Only use one of these values: 'sm', 'md', 'lg', 'xl'
# SEE: https://getbootstrap.com/docs/4.0/components/navbar/#responsive-behaviors
# FAQ: A falsy value will trigger default logic for nav width
PORTAL_NAV_WIDTH = False

# using container name to avoid cep.dev dns issues locally
# CEP_AUTH_VERIFICATION_ENDPOINT = https://hostname.tacc.utexas.edu # Dev/Prod/Etc
CEP_AUTH_VERIFICATION_ENDPOINT = 'http://django:6000'               # Local



########################
# TACC: SOCIAL MEDIA
########################

PORTAL_SOCIAL_SHARE_PLATFORMS = []
# PORTAL_SOCIAL_SHARE_PLATFORMS = ['linkedin', 'instagram', 'facebook', 'bluesky', 'email']

########################
# TACC: STYLES
########################

PORTAL_STYLES = []
# PORTAL_STYLES = [{
#     "is_remote": True,
#     "path": "https://cdn.jsdelivr.net/gh/TACC/Core-CMS-Custom@2cdc59f/example_cms/src/apps/example_app/static/example_app/css/example_app.css",
# }]

# Only use integer numbers (not "v1", not "0.11.0"),
# so templates can load based on simple comparisons
TACC_CORE_STYLES_VERSION = 2

########################
# DJANGOCMS_BLOG: TACC
########################

# Only effective with a DJANGOCMS_BLOG
# SEE: https://github.com/TACC/Core-CMS/blob/ff6c727/taccsite_cms/settings_custom.example.py#L139-L185

PORTAL_BLOG_SHOW_CATEGORIES = True
PORTAL_BLOG_SHOW_TAGS = True
# To flag posts of certain category or tag, so template can take special action
PORTAL_BLOG_CUSTOM_MEDIA_POST_CATEGORY = 'sample_value_e_g__mutlimedia__'
PORTAL_BLOG_SHOW_ABSTRACT_TAG = 'sample_value_e_g__redirect__'

PORTAL_BLOG_CATEGORY_ORDER = []
# PORTAL_BLOG_CATEGORY_ORDER = ['press-release', 'feature-story', 'multimedia', 'podcast']

########################
# DJANGO & DJANGO_CMS & TACC
########################

# Application definition
ROOT_URLCONF = 'taccsite_cms.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'taccsite_cms', 'static'),
    # os.path.join(BASE_DIR, 'taccsite_cms', 'en', 'static'),
) + tuple(glob(
    os.path.join(BASE_DIR, 'taccsite_custom', '*', 'static')
))

# Serve UI Demo (if it exists) at .../ui
ui_demo_dir = os.path.join(BASE_DIR, 'taccsite_ui', 'dist')
if os.path.exists(ui_demo_dir):
    STATICFILES_DIRS += (('ui', ui_demo_dir),)

# User Uploaded Files Location.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # FAQ: List custom directory first, so custom templates take precedence
        # SEE: https://docs.djangoproject.com/en/2.2/topics/templates/#configuration
        'DIRS': glob(
            os.path.join(BASE_DIR, 'taccsite_custom')
        ) + [
            os.path.join(BASE_DIR, 'taccsite_cms', 'templates')
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'django_settings_export.settings_export'
            ],
            'libraries': {
                # Unnecessary but explicit
                # SEE: https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#code-layout
                'custom_portal_settings': 'taccsite_cms.templatetags.custom_portal_settings',
                'tacc_uri_shortcuts': 'taccsite_cms.templatetags.tacc_uri_shortcuts',
            },
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'taccsite_cms', 'locale'),
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

# Application definition

INSTALLED_APPS = [
    # optional, but used in most projects
    'djangocms_admin_style',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # customize 'django.contrib.staticfiles'
    # SEE: https://stackoverflow.com/q/57921970/11817077
    # 'django.contrib.staticfiles',
    'taccsite_cms.django.contrib.staticfiles_custom.apps.TaccStaticFilesConfig',
    'django.contrib.messages',

    # key django CMS modules
    'cms',
    'menus',
    'sekizai',
    'treebeard',  # Replaces mptt.

    # the default CKEditor - optional, but used in most projects
    'djangocms_text_ckeditor',

    # Django Filer - optional, but used in most projects
    'filer',
    'easy_thumbnails',

    # required by django CMS Blog
    'meta',
    'djangocms_page_meta',

    # some content plugins - optional, but used in most projects
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_transfer',
    'djangocms_video',
    'djangocms_icon',

    # optional django CMS Bootstrap 4 modules
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',

    # miscellaneous
    'aldryn_apphooks_config',  # search index & django CMS Blog
    'test_without_migrations', # run tests faster

] + form_plugin_INSTALLED_APPS + [

    # core TACC CMS
    # HELP: If this were top of list, would TACC/Core-CMS/pull/169 fix break?
    'taccsite_cms',
    'common_apps.email_management',

    # django CMS Bootstrap
    # IDEA: Extend Bootstrap apps instead of overwrite
    'taccsite_cms.contrib.bootstrap4_djangocms_link',
    'taccsite_cms.contrib.bootstrap4_djangocms_picture',

    # TACC CMS Plugins
    'djangocms_tacc_image_gallery',
    # TODO: Use https://github.com/wesleyboar/Core-CMS-Plugin-System-Monitor
    'taccsite_cms.contrib.taccsite_system_monitor',

    # TACC CMS Plugins - DECPRECATED
    'taccsite_cms.contrib.taccsite_blockquote',
    'taccsite_cms.contrib.taccsite_callout',
    'taccsite_cms.contrib.taccsite_sample',
    'taccsite_cms.contrib.taccsite_offset',
    'taccsite_cms.contrib.taccsite_system_specs',
    'taccsite_cms.contrib.taccsite_data_list'
]

# Convert list of paths to list of dotted module names


def get_subdirs_as_module_names(path):
    module_names = []
    for entry in os.scandir(path):
        is_app = (
            entry.path.find('_readme') == -1 and # explains common project dirs
            entry.path.find('-org') == -1 and    # deprecated Texascale templates
            entry.path.find('-cms') == -1 and    # deprecated project templates
            entry.path.find('docs') == -1        # documentation beyond README
        )
        if entry.is_dir() and is_app:
            # FAQ: There are different root paths to tweak:
            #      - Containers use `/code/…`
            #      - Python Venvs use `/srv/taccsite/…`
            module_name = entry.path \
                .replace(os.path.sep + 'code' + os.path.sep, '') \
                .replace(os.path.sep + 'srv' + os.path.sep + 'taccsite' + os.path.sep, '') \
                .replace(os.path.sep, '.')
            module_names.append(module_name)
    return module_names


# Append CMS project paths as module names to INSTALLED_APPS
# FAQ: This automatically looks into `/taccsite_custom` and creates an "App" for each directory within
CUSTOM_CMS_DIR = os.path.join(BASE_DIR, 'taccsite_custom')

INSTALLED_APPS_APPEND = get_subdirs_as_module_names(CUSTOM_CMS_DIR)
INSTALLED_APPS = INSTALLED_APPS + INSTALLED_APPS_APPEND

MIGRATION_MODULES = {}
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    # Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    # Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS = [
    576, 768, 992, 1200, 1400, 1680, 1920
]
DJANGOCMS_PICTURE_RATIO = 1.618
DJANGOCMS_PICTURE_ALIGN = [
    ('left', _('Align left')),
    ('right', _('Align right')),
    ('center', _('Align center')),
]

# FILE UPLOAD VALUES MUST BE SET!
# Set in correlation with the `client_max_body_size    20m;` value in /etc/nginx/proxy.conf.
# A problem comes from Django's usage of tempfile, which enforces new files to have permission
# 0600 and Django doesn't fix it unless FILE_UPLOAD_PERMISSIONS is defined.
# A tempfile is used when upload exceeds FILE_UPLOAD_MAX_MEMORY_SIZE.
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_MAX_MEMORY_SIZE = 20000000  # 20MB

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']

########################
# PLUGIN SETTINGS
########################

# SEE: https://github.com/django-cms/djangocms-bootstrap4
DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = [
    (_('Container'), (
        ('container', _('Container')), # default
        (
            'container  o-section o-section--style-light',
            _('Fluid, Light section')
        ),
        (
            'container  o-section o-section--style-dark',
            _('Fluid, Dark section')
        ),
    )),
    (_('Fluid container'), (
        ('container-fluid', _('Fluid')), # default
        (
            'container-fluid  o-section o-section--style-light',
            _('Fluid, Light section')
        ),
        (
            'container-fluid  o-section o-section--style-dark',
            _('Fluid, Dark section')
        ),
    )),
    (_('No container'), (
        (
            'o-section o-section--style-light',
            _('Fluid, Light section')
        ),
        (
            'o-section o-section--style-dark',
            _('Fluid, Dark section')
        ),
    )),
]

# https://github.com/django-cms/djangocms-style
DJANGOCMS_STYLE_CHOICES = [
    'card',
    'card--plain',
    'card--standard',
    'card--image-top',
    'card--image-bottom',
    'card--image-right',
    'card--image-left',
    'section',
    'section--light',
    'section--muted',
    'section--dark',
    'o-section',
    'o-section o-section--style-light',
    'o-section o-section--style-muted',
    'o-section o-section--style-dark',
    'c-callout',
    'c-recognition c-recognition--style-light',
    'c-recognition c-recognition--style-dark',
    'c-nav', # bare-bones instance
    'c-nav c-nav--boxed',
]
DJANGOCMS_STYLE_TAGS = [
    # Even though <div> is often NOT the most semantic choice;
    # CMS editor may neglect tag, any other tag could be inaccurate,
    # and <div> is never inaccurate; so <div> is placed first 😞
    # RFE: Support automatically choosing tag based on class name
    # SEE: https://github.com/TACC/Core-CMS/pull/432
    'div',
    # Ordered by expected usage
    'section', 'article', 'header', 'footer', 'aside', 'nav',
    # Not expected but not unreasonable
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]

# https://github.com/nephila/django-meta
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_SCHEMAORG_PROPERTIES = True

# https://github.com/django-cms/djangocms-text-ckeditor
CKEDITOR_SETTINGS = {
    'autoParagraph': False,
    'stylesSet': 'default:/static/js/addons/ckeditor.wysiwyg.js',
    'contentsCss': ['/static/djangocms_text_ckeditor/ckeditor/contents.css'],
}

# https://github.com/django-cms/djangocms-video
DJANGOCMS_VIDEO_TEMPLATES = [
    ('responsive-auto', _('Responsive - Automatic')),
    ('responsive-16by9', _('Responsive - 16 by 9')),
    ('responsive-4by3', _('Responsive - 4 by 3')),
    ('responsive-1by1', _('Responsive - 1 by 1')),
    ('responsive-21by9', _('Responsive - 21 by 9')),
]

# DJANGOCMS_ICON SETTINGS
# https://github.com/django-cms/djangocms-icon

ICON_PATH = os.path.join('taccsite_cms', 'static', 'site_cms', 'img', 'icons')

LOGO_ICONFILE = os.path.join(BASE_DIR, ICON_PATH, 'logos.json')
with open(LOGO_ICONFILE, 'r') as f:
    LOGO_ICONS = f.read()

CORTAL_ICONFILE = os.path.join(BASE_DIR, ICON_PATH, 'cortal.json')
with open(CORTAL_ICONFILE, 'r') as f:
    CORTAL_ICONS = f.read()

DJANGOCMS_ICON_SETS = [
    # The SVG icon set must be first or icon selection is not remembered on edit
    # HELP: Icon previews are blank if editor switches from SVG set to icon set
    # https://github.com/django-cms/djangocms-icon/issues/9
    (LOGO_ICONS, '', _('Logo SVGs')),
    (CORTAL_ICONS, 'icon', _('TACC "Cortal" Icons')),
]



########################
# SEARCH
########################

# To support any search
PORTAL_SEARCH_PATH = '/search'

# To support Google search
# PORTAL_SEARCH_QUERY_PARAM_NAME = 'q'
# PORTAL_ES_ENABLED = False

# To support Elasticsearch
PORTAL_SEARCH_QUERY_PARAM_NAME = 'query_string'
PORTAL_ES_ENABLED = True



########################
# SETTINGS IMPORT
########################

try:
    from taccsite_cms.settings_custom import *
    import taccsite_cms.settings_custom as settings_custom
except ModuleNotFoundError:
    settings_custom = []

try:
    from taccsite_cms.secrets import *
except ModuleNotFoundError:
    pass

try:
    from taccsite_cms.settings_local import *
    import taccsite_cms.settings_local as settings_local
except ModuleNotFoundError:
    settings_local = []

try:
    from taccsite_cms import custom_app_settings
    INSTALLED_APPS += getattr(custom_app_settings, 'CUSTOM_APPS', [])
    STATICFILES_DIRS += getattr(custom_app_settings , 'STATICFILES_DIRS', ())
    MIDDLEWARE += getattr(custom_app_settings , 'CUSTOM_MIDDLEWARE', ())
except ImportError:
    pass

########################
# SETTINGS DEPRECATED
# TODO: Make clients not use nor set these
########################

deprecated_SETTINGS_EXPORT = []

# For header_branding.html
deprecated_SETTINGS_EXPORT += ['BRANDING']
if 'BRANDING' not in locals():
    BRANDING = False

# For header_logo.html
deprecated_SETTINGS_EXPORT += ['LOGO']
if 'LOGO' not in locals():
    LOGO = False

# For clients
old_setting_names = [
    'FAVICON'
    'INCLUDES_CORE_PORTAL',
    'INCLUDES_PORTAL_NAV',
    'INCLUDES_SEARCH_BAR',
    'TACC_BLOG_SHOW_CATEGORIES',
    'TACC_BLOG_SHOW_TAGS',
    'TACC_BLOG_CUSTOM_MEDIA_POST_CATEGORY',
    'TACC_BLOG_SHOW_ABSTRACT_TAG',
    'TACC_BLOG_CATEGORY_ORDER',
    'TACC_SOCIAL_SHARE_PLATFORMS',
    'SEARCH_PATH',
    'SEARCH_QUERY_PARAM_NAME',
]
for old_setting_name in old_setting_names:
    if old_setting_name in locals() or \
        hasattr(settings_custom, old_setting_name) or \
        hasattr(settings_local, old_setting_name):
            if old_setting_name.startswith('TACC_'):
                stripped_setting_name = old_setting_name.replace('TACC_', '')
                locals()['PORTAL_' + stripped_setting_name] = locals()[old_setting_name]
            if old_setting_name.startswith('SEARCH_'):
                locals()['PORTAL_' + old_setting_name] = locals()[old_setting_name]
            if 'FAVICON' == old_setting_name:
                deprecated_SETTINGS_EXPORT += ['FAVICON']
            if 'INCLUDES_CORE_PORTAL' == old_setting_name:
                PORTAL_IS_TACC_CORE_PORTAL = INCLUDES_CORE_PORTAL
            if 'INCLUDES_PORTAL_NAV' == old_setting_name:
                PORTAL_HAS_LOGIN = INCLUDES_PORTAL_NAV
            if 'INCLUDES_SEARCH_BAR' == old_setting_name:
                PORTAL_HAS_SEARCH = INCLUDES_SEARCH_BAR

# For clients using Elasticsearch
if PORTAL_ES_ENABLED:
    from taccsite_cms._settings.es_search import *
    from taccsite_cms._settings.es_search import (
        _INSTALLED_APPS as es_search_INSTALLED_APPS
    )
    index = INSTALLED_APPS.index('aldryn_apphooks_config')
    INSTALLED_APPS[index:index] = es_search_INSTALLED_APPS

########################
# SETTINGS EXPORT
########################

SETTINGS_EXPORT_VARIABLE_NAME = 'settings'

SETTINGS_EXPORT = deprecated_SETTINGS_EXPORT + [
    'DEBUG',
    'TACC_CORE_STYLES_VERSION',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD',
    'PORTAL_BRANDING',
    'PORTAL_LOGO',
    'PORTAL_FAVICON',
    'PORTAL_IS_TACC_CORE_PORTAL',
    'PORTAL_HAS_LOGIN',
    'PORTAL_HAS_SEARCH',
    'PORTAL_NAV_WIDTH',
    'PORTAL_STYLES',
    'PORTAL_BLOG_SHOW_CATEGORIES',
    'PORTAL_BLOG_SHOW_TAGS',
    'PORTAL_BLOG_CUSTOM_MEDIA_POST_CATEGORY',
    'PORTAL_BLOG_SHOW_ABSTRACT_TAG',
    'PORTAL_BLOG_CATEGORY_ORDER',
    'PORTAL_SOCIAL_SHARE_PLATFORMS',
    'PORTAL_SEARCH_PATH',
    'PORTAL_SEARCH_QUERY_PARAM_NAME',
]
