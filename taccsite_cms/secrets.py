########################
# DJANGO SETTINGS
########################

_SECRET_KEY = '1y^hda&p5-3@jdsi^k7bzqiif%%26g$2q*hw9o@j6s^$&y0*$7'
_DEBUG = True       # False for Prod.
# Specify allowed hosts or use an asterisk to allow any host and simplify the config.
# _ALLOWED_HOSTS = ['cms-template01.tacc.utexas.edu', '129.114.60.172', '0.0.0.0', 'localhost', '127.0.0.1']
_ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']

########################
# CUSTOM SITE SETTINGS
########################

_NAVIGATION_PARTIAL_ROOT = 'nav_branding_partials'
_NAVIGATION_PARTIAL_TEMPLATE = 'nav.branding.texascale.v2.html'
_NAVIGATION_TEMPLATE = 'nav_branding_partials/nav.branding.texascale.v2.html'

########################
# DATABASE SETTINGS
########################

_DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
_DATABASE_NAME = 'taccsite'
_DATABASE_USERNAME = 'postgresadmin'
_DATABASE_PASSWORD = 'T@CC373rn@1'
_DATABASE_HOST = 'localhost'
_DATABASE_PORT = '5432'

########################
# DJANGO CMS SETTINGS
########################

# CMS Site (allows for multiple sites on a single CMS)
_SITE_ID = 1
_CMS_TEMPLATES = (
    # Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

########################
# GOOGLE ANALYTICS
########################

# To use during dev, Tracking Protection in browser needs to be turned OFF.
_GOOGLE_ANALYTICS_PROPERTY_ID = "UA-XXXYYYZZZZ-#"
_GOOGLE_ANALYTICS_PRELOAD = True
