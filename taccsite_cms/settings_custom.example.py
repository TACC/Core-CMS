'''
A `settings_custom.py` file can override default values in settings.py

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
# DJANGO CMS SETTINGS
########################

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home_portal.html', 'Standard Portal Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack'),
)

########################
# TACC: BRANDING
########################

_CUSTOM_BRANDING = [
    "sgci",
    "brainmap-cms/img/org_logos/sgci-logo-sans-text.svg",
    "branding-logo--short",
    "https://sciencegateways.org/",
    "_blank",
    "SGCI Logo",
    "anonymous",
    "True",
]

BRANDING = [ TACC_BRANDING, UTEXAS_BRANDING, NSF_BRANDING, _CUSTOM_BRANDING ]

########################
# TACC: LOGOS
########################

LOGO =  [
    "brainmap",
    "brainmap-cms/img/org_logos/brainmap-logo.png",
    "",
    "https://brainmap.org",
    "_self",
    "BrainMap Logo",
    "anonymous",
    "True"
]

FAVICON = {
    "img_file_src": "brainmap-cms/img/org_logos/favicon.ico"
}

########################
# BLOG & SOCIAL METADATA
########################

# Install required apps
INSTALLED_APPS += [
    # Blog/News
    # 'filer',              # already added
    # 'easy_thumbnails',    # already added
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',                 # also supports `djangocms_page_meta`
    'sortedm2m',
    'djangocms_blog',

    # Metadata
    'djangocms_page_meta',
]
# CAVEAT: 'taggit_autosuggest' requires the following is added to `urls.py`
"""
urlpatterns += [
    # Support `taggit_autosuggest` (from `djangocms-blog`)
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
"""

# Metadata: Configure
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_GOOGLEPLUS_PROPERTIES = True # django-meta 1.x+
# META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+

# Blog/News: Set custom paths for templates
BLOG_PLUGIN_TEMPLATE_FOLDERS = (
    ('plugins/default', 'Default template'),    # i.e. `templates/djangocms_blog/plugins/default/`
    ('plugins/default-clone', 'Clone of default template'),  # i.e. `templates/djangocms_blog/plugins/default-clone/`
)

# Blog/News: Change default values for the auto-setup of one `BlogConfig`
# SEE: https://github.com/nephila/djangocms-blog/issues/629
BLOG_AUTO_SETUP = True
BLOG_AUTO_HOME_TITLE ='Home'
BLOG_AUTO_BLOG_TITLE = 'News'
BLOG_AUTO_APP_TITLE = 'News'
