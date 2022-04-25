
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
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

SECRET_KEY = 'CHANGE_ME'
def gettext(s): return s


DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True       # False for Prod.

# Specify allowed hosts or use an asterisk to allow any host and simplify the config.
# ALLOWED_HOSTS = ['hostname.tacc.utexas.edu', 'host.ip.v4.address', '0.0.0.0', 'localhost', '127.0.0.1']   # In production.
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']   # In development.

# Requires django-auth-ldap ≥ 2.0.0
LDAP_ENABLED = True

# Default portal authorization verification endpoint.
CEP_AUTH_VERIFICATION_ENDPOINT = 'localhost'  # 'https://0.0.0.0:8000'

########################
# DATABASE SETTINGS
########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'PORT': '5432',
        'NAME': 'taccsite',
        'USER': 'postgresadmin',
        'PASSWORD': 'taccforever',  # Change before live deployment.
        'HOST': 'core_cms_postgres'
    }
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "taccsite_cms.remote_cms_auth.CorePortalAuthBackend",
    "django_auth_ldap.backend.LDAPBackend"
]

''' LDAP Auth Settings '''
AUTH_LDAP_SERVER_URI = "ldap://ldap.tacc.utexas.edu"
AUTH_LDAP_CONNECTION_OPTIONS = {ldap.OPT_REFERRALS: 0}
AUTH_LDAP_START_TLS = True
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_AUTHORIZE_ALL_USERS = True

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=People,dc=tacc,dc=utexas,dc=edu", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

SITE_ID = 1

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),
)

CMS_PERMISSION = True

########################
# TACC: GOOGLE ANALYTICS
########################

# To use during dev, Tracking Protection in browser needs to be turned OFF.
GOOGLE_ANALYTICS_PROPERTY_ID = "UA-123ABC@%$&-#"
GOOGLE_ANALYTICS_PRELOAD = True

########################
# CMS FORMS
########################

# Create CMS Forms
# SEE: https://pypi.org/project/djangocms-forms/
# SEE: https://www.google.com/recaptcha/admin/create
DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY = ""
DJANGOCMS_FORMS_RECAPTCHA_SECRET_KEY = ""

########################
# ELASTICSEARCH
########################

ES_AUTH = 'username:password'
ES_HOSTS = 'http://elasticsearch:9200'
ES_INDEX_PREFIX = 'cms-dev-{}'
ES_DOMAIN = 'http://localhost:8000'

########################
# TACC: (DEPRECATED)
########################

"""
Optional theming of CMS (certain themes may only affect some elements)
Usage:
- None (standard theme)
- 'has-dark-logo'
"""
THEME = None

########################
# TACC: BRANDING
########################

TACC_BRANDING = [
    "tacc",
    "site_cms/img/org_logos/tacc-white.png",
    "branding-tacc",
    "https://www.tacc.utexas.edu/",
    "_blank",
    "TACC Logo",
    "anonymous",
    "True"
]

UTEXAS_BRANDING = [
    "utexas",
    "site_cms/img/org_logos/utaustin-white.png",
    "branding-utaustin",
    "https://www.utexas.edu/",
    "_blank",
    "University of Texas at Austin Logo",
    "anonymous",
    "True"
]

NSF_BRANDING = [
    "nsf",
    "site_cms/img/org_logos/nsf-white.png",
    "branding-nsf",
    "https://www.nsf.gov/",
    "_blank",
    "NSF Logo",
    "anonymous",
    "True"
]

BRANDING = [TACC_BRANDING, UTEXAS_BRANDING]

########################
# TACC: LOGOS
########################

LOGO = [
    "portal",
    "site_cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "site_cms/img/favicons/favicon.ico"
}

########################
# TACC: PORTAL
########################

INCLUDES_CORE_PORTAL = True

LOGOUT_REDIRECT_URL = '/'

# using container name to avoid cep.dev dns issues locally
# this will need to be updated for dev/pprd/prod systems
# for example, CEP_AUTH_VERIFICATION_ENDPOINT=https://dev.cep.tacc.utexas.edu
CEP_AUTH_VERIFICATION_ENDPOINT = 'http://django:6000'

########################
# CLIENT BUILD SETTINGS
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
                # NOTE: These may be unnecessary alternative config, because taccsite_cms is in INSTALLED_APPS, but are comfortably explicit
                # SEE: https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/#code-layout
                'custom_portal_settings': 'taccsite_cms.templatetags.custom_portal_settings',
                'tacc_uri_shortcuts': 'taccsite_cms.templatetags.tacc_uri_shortcuts',
                'preferred_tag_for_class': 'taccsite_cms.templatetags.preferred_tag_for_class',
            },
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
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

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # Customize 'django.contrib.staticfiles'
    # SEE: https://stackoverflow.com/q/57921970/11817077
    # 'django.contrib.staticfiles',
    'taccsite_cms.django.contrib.staticfiles_custom',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',  # Replaces mptt.
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
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
    'haystack',
    'aldryn_apphooks_config',
    'test_without_migrations',
    'taccsite_cms',
    'taccsite_cms.contrib.bootstrap4_djangocms_link',
    'taccsite_cms.contrib.bootstrap4_djangocms_picture',
    # FP-1231: Convert our CMS plugins to stand-alone apps
    'taccsite_cms.contrib.taccsite_blockquote',
    'taccsite_cms.contrib.taccsite_callout',
    'taccsite_cms.contrib.taccsite_sample',
    'taccsite_cms.contrib.taccsite_offset',
    'taccsite_cms.contrib.taccsite_system_specs',
    'taccsite_cms.contrib.taccsite_system_monitor',
    'taccsite_cms.contrib.taccsite_data_list'
]

# Convert list of paths to list of dotted module names


def get_subdirs_as_module_names(path):
    module_names = []
    for entry in os.scandir(path):
        is_app = entry.path.find('_readme') == -1
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

# FILE UPLOAD VALUES MUST BE SET!
# Set in correlation with the `client_max_body_size    20m;` value in /etc/nginx/proxy.conf.
# A problem comes from Django's usage of tempfile, which enforces new files to have permission
# 0600 and Django doesn't fix it unless FILE_UPLOAD_PERMISSIONS is defined.
# A tempfile is used when upload exceeds FILE_UPLOAD_MAX_MEMORY_SIZE.
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_MAX_MEMORY_SIZE = 20000000  # 20MB

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']

# Djangocms Forms Settings.
# SEE: https://github.com/mishbahr/djangocms-forms#configuration
DJANGOCMS_FORMS_PLUGIN_MODULE = ('Generic')
DJANGOCMS_FORMS_PLUGIN_NAME = ('Form')

DJANGOCMS_FORMS_TEMPLATES = (
    ('djangocms_forms/form_template/default.html', ('Default')),
)
DJANGOCMS_FORMS_USE_HTML5_REQUIRED = False

DJANGOCMS_FORMS_REDIRECT_DELAY = 1

# Elasticsearch Indexing
HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter', ]
HAYSTACK_SIGNAL_PROCESSOR = 'taccsite_cms.signal_processor.RealtimeSignalProcessor'
ALDRYN_SEARCH_DEFAULT_LANGUAGE = 'en'
ALDRYN_SEARCH_REGISTER_APPHOOK = True
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': ES_HOSTS,
        'INDEX_NAME': ES_INDEX_PREFIX.format('cms'),
        'KWARGS': {'http_auth': ES_AUTH}
    }
}

SETTINGS_EXPORT_VARIABLE_NAME = 'settings'

FEATURES = ''

########################
# PLUGIN SETTINGS
########################

# https://github.com/django-cms/djangocms-style
DJANGOCMS_STYLE_CHOICES = [
    # https://cep.tacc.utexas.edu/design-system/ui-patterns/o-section/
    'o-section o-section--style-light',
    'o-section o-section--style-dark',
    # https://cep.tacc.utexas.edu/design-system/ui-patterns/c-callout/
    'c-callout',
    # https://cep.tacc.utexas.edu/design-system/ui-patterns/c-recognition/
    'c-recognition c-recognition--style-light',
    'c-recognition c-recognition--style-dark',
]
DJANGOCMS_STYLE_TAGS_DEFAULT = 'Automatic'
DJANGOCMS_STYLE_TAGS = [
    # CMS editor may neglect tag so we support intelligent tag choice
    # SEE: taccsite_cms/templatetags/preferred_tag_for_class.py
    DJANGOCMS_STYLE_TAGS_DEFAULT,
    # Ordered by expected usage
    'section', 'article', 'header', 'footer', 'aside', 'div',
    # Not expected but not unreasonable
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]

########################
# SETTINGS IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_custom import *
except:
    None
    # do nothing

try:
    from taccsite_cms.secrets import *
except:
    None
    # do nothing

try:
    from taccsite_cms.settings_local import *
except:
    None
    # do nothing

SETTINGS_EXPORT = [
    'DEBUG',
    'FEATURES',
    'THEME',
    'BRANDING',
    'LOGO',
    'FAVICON',
    'INCLUDES_CORE_PORTAL',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD',
    'DJANGOCMS_STYLE_TAGS_DEFAULT'
]
