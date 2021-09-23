
'''

settings_custom.py file can be used to override default values in settings.py

The settings_custom.py file is loaded after default settings but before settings assignment is complete,
giving us the opportunity to override settings in either settings_custom.py (usually set in custom sites)
or in settings_local.py (usually used in a local dev environment).

To override a setting,
simply copy/paste the default settings and set the new/custom values

If a setting override is for a custom site in an existing submodule, the change is made in
the settings_custom.py file of that submodules site directory and (if not a secret) can be committed


Unless modifying default behavior for the default cms and all custom sites (which probably means that
setting should be in the settings.py file), the settings_custom.py file that should be modified is
the one in the appropriate taccsite_custom site directory.

'''

# For example if we want to change LDAP auth settings for a custome site, let's say frontera-cms
# we simply copy the setting from settings.py, and
# assign the new value in "Core-CMS/taccsite_custom/frontera-cms/settings_custom.py"
''' Example LDAP Auth Setting change where we just changing the ldap url '''
AUTH_LDAP_SERVER_URI = "ldap://cluster.ldap.tacc.utexas.edu"

#The same goes for other more commonly customized values like below
# A customization to this default would be applied in settings_custom.py of the appropriate custom site
PORTAL_LOGO = [
    "portal",
    "site_cms/img/org_logos/portal.png",
    "",
    "/",
    "_self",
    "Portal Logo",
    "anonymous",
    "True"
]

LOGO = PORTAL_LOGO

CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
    ('fullwidth.html', 'Full Width'),

    ('home_portal.html', 'Standard Portal Homepage'),

    ('guide.html', 'Guide'),
    ('guides/getting_started.html', 'Guide: Getting Started'),
    ('guides/data_transfer.html', 'Guide: Data Transfer'),
    ('guides/data_transfer.globus.html', 'Guide: Globus Data Transfer'),
    ('guides/portal_technology.html', 'Guide: Portal Technology Stack')
)
