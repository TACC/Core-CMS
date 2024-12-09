'''
A `settings_local.py` file can override default values in `settings.py` and `settings_custom.py`.

For a detailed walkthrough on overriding settings, see `settings_custom.example.py`:
https://github.com/TACC/Core-CMS/blob/main/taccsite_cms/settings_custom.example.py
'''

# https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '*']   # Local
# ALLOWED_HOSTS = ['hostname.tacc.utexas.edu', 'client.org'] # Dev/Prod/Etc

# To manage remote CMS authentication
CEP_AUTH_VERIFICATION_ENDPOINT = 'http://django:6000'
LOGIN_REDIRECT_URL = '/'

# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DEBUG
DEBUG = True

# To hide error about using Google Recaptcha test keys
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# To disable the Core-Portal integration
# IMPORTANT: Do not disable by default, because [Core-Portal clones this file](https://github.com/TACC/Core-Portal/pull/1034)
# PORTAL_IS_TACC_CORE_PORTAL = False
# PORTAL_HAS_LOGIN = False
