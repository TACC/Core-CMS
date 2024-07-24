'''
A `settings_local.py` file can override default values in `settings.py` and `settings_custom.py`.

For a detailed walkthrough on overriding settings, see `settings_custom.example.py`:
https://github.com/TACC/Core-CMS/blob/main/taccsite_cms/settings_custom.example.py
'''

# To hide error about using Google Recaptcha test keys
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# To disable the Core-Portal integration
PORTAL_IS_TACC_CORE_PORTAL = False
PORTAL_HAS_LOGIN = False
