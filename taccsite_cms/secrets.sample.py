
########################
# DJANGO SETTINGS
########################

_SECRET_KEY = 'Change Me'
_DEBUG = True
_ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']

########################
# CUSTOM SITE SETTINGS
########################

# Replace ______ with correct filename for the project
_NAVIGATION_PARTIAL_ROOT = 'nav_branding_partials'
_NAVIGATION_PARTIAL_TEMPLATE = 'nav.branding.______.v2.html'
_NAVIGATION_TEMPLATE = 'nav_branding_partials/nav.branding.______.v2.html'

########################
# DATABASE SETTINGS
########################

_DATABASE_ENGINE = 'django.db.backends.postgresql'
_DATABASE_NAME = 'taccsite'
_DATABASE_USERNAME = 'taccsite'
_DATABASE_PASSWORD = 'taccsite'
_DATABASE_HOST = 'taccsite_postgres'
_DATABASE_PORT = '' # 5432 (default)

########################
# DJANGO CMS SETTINGS
########################

# CMS Site (allows for multiple sites on a single CMS)
_SITE_ID = 1
_CMS_TEMPLATES = (
    # Customize this per project
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)
# Forms Plugin
_DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY = ''
_DJANGOCMS_FORMS_RECAPTCHA_SECRET_KEY = ''

########################
# GOOGLE ANALYTICS
########################

# To use during dev, Tracking Protection in browser needs to be turned OFF.
_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-XXXYYYZZZZ-#"
_GOOGLE_ANALYTICS_PRELOAD = True
