"""Configure django authentication"""

import ldap

########################
# DJANGO
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth
########################

# To disable LDAP:
#
# 0. Edit custom or local settings for CMS project.
# 1. Set 'LDAP_ENABLED = False'.
# 2. Duplicate the 'AUTHENTICATION_BACKENDS' setting.
# 3. Remove its '...LDAPBackend' entry.
# 4. If 'INCLUDES_CORE_PORTAL = False', remove '...CorePortalAuthBackend' entry.
#
# RFE: Use INCLUDES_CORE_PORTAL to toggle '...CorePortalAuthBackend'.

# Requires django-auth-ldap ≥ 2.0.0
LDAP_ENABLED = True

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "taccsite_cms.remote_cms_auth.CorePortalAuthBackend",
    "django_auth_ldap.backend.LDAPBackend"
]

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
