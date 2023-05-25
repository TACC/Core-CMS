
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

SECRET_KEY = 'CHANGE_ME'
def gettext(s): return s


DATA_DIR = os.path.dirname(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True       # False for Prod.

# Specify allowed hosts or use an asterisk to allow any host and simplify the config.
# ALLOWED_HOSTS = ['hostname.tacc.utexas.edu', 'host.ip.v4.address', '0.0.0.0', 'localhost', '127.0.0.1']   # In production.
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']   # In development.

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
# (some) CMS SETTINGS
########################

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
# TACC: SEARCH
########################

SEARCH_QUERY_PARAM_NAME = 'query_string'

########################
# ELASTICSEARCH
########################

ES_AUTH = 'username:password'
ES_HOSTS = 'http://elasticsearch:9200'
ES_INDEX_PREFIX = 'cms-dev-{}'
ES_DOMAIN = 'http://localhost:8000'

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
INCLUDES_PORTAL_NAV = True
INCLUDES_SEARCH_BAR = True

LOGOUT_REDIRECT_URL = '/'

# using container name to avoid cep.dev dns issues locally
# this will need to be updated for dev/pprd/prod systems
# for example, CEP_AUTH_VERIFICATION_ENDPOINT=https://dev.cep.tacc.utexas.edu
CEP_AUTH_VERIFICATION_ENDPOINT = 'http://django:6000'

########################
# TACC: NEWS/BLOG
########################

TACC_BLOG_SHOW_CATEGORIES = True
TACC_BLOG_SHOW_TAGS = True
# To flag posts of certain category or tag, so template can take special action
TACC_BLOG_CUSTOM_MEDIA_POST_CATEGORY = 'sample_value_e_g__mutlimedia__'
TACC_BLOG_SHOW_ABSTRACT_TAG = 'sample_value_e_g__redirect__'



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
)) + (
    ('ui', os.path.join(BASE_DIR, 'taccsite_ui', 'dist')),
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

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
    'taccsite_cms.django.contrib.staticfiles_custom',
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
    'haystack',                # search index
    'aldryn_apphooks_config',  # search index & django CMS Blog
    'test_without_migrations', # run tests faster

] + form_plugin_INSTALLED_APPS + [

    # core TACC CMS
    # HELP: If this were top of list, would TACC/Core-CMS/pull/169 fix break?
    'taccsite_cms',

    # django CMS Blog requirements
    # IDEA: Extend Bootstrap apps instead of overwrite
    'taccsite_cms.contrib.bootstrap4_djangocms_link',
    'taccsite_cms.contrib.bootstrap4_djangocms_picture',
    # TODO: Deprecate these plugins (except taccsite_system_monitor)
    # TODO: For taccsite_system_monitor use repo package:
    #       https://github.com/wesleyboar/Core-CMS-Plugin-System-Monitor
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

SETTINGS_EXPORT_VARIABLE_NAME = 'settings'

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
    # https://cep.tacc.utexas.edu/design-system/ui-patterns/c-nav/
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
# IMPORT & EXPORT
########################

try:
    from taccsite_cms.settings_custom import *
except ModuleNotFoundError:
    pass

try:
    from taccsite_cms.secrets import *
except ModuleNotFoundError:
    pass

try:
    from taccsite_cms.settings_local import *
except ModuleNotFoundError:
    pass

try:
    from taccsite_cms import custom_app_settings
    INSTALLED_APPS += getattr(custom_app_settings, 'CUSTOM_APPS', [])
    STATICFILES_DIRS += getattr(custom_app_settings , 'STATICFILES_DIRS', ())
    MIDDLEWARE += getattr(custom_app_settings , 'CUSTOM_MIDDLEWARE', ())
except ImportError:
    pass

SETTINGS_EXPORT = [
    'DEBUG',
    'BRANDING',
    'LOGO',
    'FAVICON',
    'INCLUDES_CORE_PORTAL',
    'INCLUDES_PORTAL_NAV',
    'INCLUDES_SEARCH_BAR',
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD',
    'TACC_BLOG_SHOW_CATEGORIES',
    'TACC_BLOG_SHOW_TAGS',
    'TACC_BLOG_CUSTOM_MEDIA_POST_CATEGORY',
    'TACC_BLOG_SHOW_ABSTRACT_TAG',
    'SEARCH_QUERY_PARAM_NAME',
]
