'''
A `settings_custom.py` file can override default values in `settings.py`.

The file is loaded after default settings but before settings assignment is complete, so we can override settings in:
- _either_ `settings_custom.py` (usually set in custom sites)
- _or_ in `settings_local.py` (usually used in a local dev environment)

To override a setting:
1. Copy/Paste the default settings.
2. Set the new/custom values.

If a setting override is for a custom CMS Project, the change is made in the `settings_custom.py` file of that project's directory and (if not a secret) can be committed.

Unless modifying default behavior for the CMS Core (and thus all custom Projects) (which probably means that setting should be in the `settings.py` file), the `settings_custom.py` file that should be modified is the one in the appropriate CMS Project directory.
'''

########################
# WALKTHROUGH
########################

# To change LDAP auth settings for a custom CMS Project (e.g. `frontera-cms`):
# 1. Copy the setting from `settings.py`
# 2. Assign the new value in `Core-CMS/taccsite_custom/frontera-cms/settings_custom.py`.
AUTH_LDAP_SERVER_URI = "ldap://cluster.ldap.tacc.utexas.edu"

# The same goes for other more commonly customized values like below.

########################
# DJANGO_CMS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home_portal.html', 'Standard Portal Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.v3.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),
)

########################
# CUSTOM PORTAL BRANDING
########################

from taccsite_cms._settings.branding import *

# Edit this config as needed for the project branding used in the navigation bar header.
CUSTOM_BRANDING = [
    "portal",
    "example_cms/img/org_logos/portal.png",
    "branding-logo--short",
    "https://cep.tacc.utexas.edu",
    "_blank",
    "Portal Logo",
    "anonymous",
    "True",
]

# Generic TACC Portals.
PORTAL_BRANDING = [ PORTAL_BRANDING_TACC, UTEXAS_BRANDING ]

# Custom-Branded Portals (Non-NSF).
# PORTAL_BRANDING = [ PORTAL_BRANDING_TACC, PORTAL_BRANDING_UTEXAS, CUSTOM_BRANDING ]

# NSF-Funded Generic TACC Portals.
# PORTAL_BRANDING = [ PORTAL_BRANDING_NSF, PORTAL_BRANDING_TACC, PORTAL_BRANDING_UTEXAS ]

# NSF-Funded & Custom-Branded Portals.
# PORTAL_BRANDING = [ PORTAL_BRANDING_NSF, PORTAL_BRANDING_TACC, PORTAL_BRANDING_UTEXAS, CUSTOM_BRANDING ]

########################
# TACC: LOGO & FAVICON
########################

# Edit this config as needed for the project logo used in the navigation bar.
# To hide logo, set `TACC_LOGO = False`.
PORTAL_LOGO = {
    "is_remote": True,
    "img_file_src": "https://cdn.jsdelivr.net/gh/TACC/Core-CMS-Custom@813aa7c/ptdatax_assets/logo.png",
    "img_class": "", # additional class names
    "link_href": "/",
    "link_target": "_self",
    "img_alt_text": "Custom CMS", # E.g. PT DataX, Frontera
    "img_crossorigin": "anonymous",
}

# Edit this config as needed for the project favicon used in the browser navbar.
# If `INCLUDES_CORE_PORTAL = True` and you set `FAVICON`, then:
# https://github.com/TACC/Core-CMS-Custom/blob/d4c93af/docs/port-project.md#has-a-core-portal
PORTAL_FAVICON = {
    "is_remote": True,
    "img_file_src": "https://cdn.jsdelivr.net/gh/TACC/Core-CMS-Custom@813aa7c/ptdatax_assets/favicon.ico",
}

########################
# SEARCH
########################

# To support Google search
PORTAL_SEARCH_QUERY_PARAM_NAME = 'q'

# To disable Elasticsearch
PORTAL_SEARCH_INDEX_IS_AUTOMATIC = False

########################
# DJANGOCMS_BLOG
########################

from taccsite_cms.settings import INSTALLED_APPS

tacc_app_index = INSTALLED_APPS.index('taccsite_cms')
INSTALLED_APPS[tacc_app_index:tacc_app_index] = [
    # 'aldryn_apphooks_config' # already in Core
    # 'filer',              # already in Core
    # 'easy_thumbnails',    # already in Core
    'parler',
    'taggit',
    'taggit_autosuggest',
    # 'meta',               # already in Core
    'sortedm2m',
    'djangocms_blog',
]
# REQ: 'taggit_autosuggest' requires the following is added to `urls.py`
# FAQ: For local Core-CMS or any Core-CMS-Custom app, add to `urls_custom.py`
"""
from django.urls import re_path, include

urlpatterns += [
    # Support `taggit_autosuggest` (from `djangocms-blog`)
    re_path(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
"""

# Paths for alternate templates that user can choose for blog-specific plugin
# - Devs can customize core templates at `templates/djangocms_blog/`.
# - Users can choose alt. templates from `templates/djangocms_blog/plugins/*`.
# - Devs can customize alt. templates at `templates/djangocms_blog/plugins/*`.
BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins', 'Default'),
    # ('plugins/alternate', 'Alternate'),
)

# Change default values for the auto-setup of one `BlogConfig`
# SEE: https://github.com/nephila/djangocms-blog/issues/629
BLOG_AUTO_SETUP = True # Set to False after setup (minimize overhead)
BLOG_AUTO_HOME_TITLE ='Home'
BLOG_AUTO_BLOG_TITLE = 'News'
BLOG_AUTO_APP_TITLE = 'News'
BLOG_AUTO_NAMESPACE = 'News'

# Miscellaneous settings
BLOG_ENABLE_COMMENTS = False

########################
# DJANGOCMS_BLOG: TACC
########################

PORTAL_BLOG_SHOW_CATEGORIES = True
PORTAL_BLOG_SHOW_TAGS = True

########################
# DJANGOCMS_BLOG: DJANGO
########################

# TACC/Core-CMS-Resources#75: Load custom urls.py so we can add urlpatterns for taggit_autosuggest
ROOT_URLCONF = 'taccsite_custom.example_cms.urls'
