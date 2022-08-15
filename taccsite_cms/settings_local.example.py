'''
A `settings_local.py` file can override default values in `settings.py` and `settings_custom.py`.

For more details about overriding settings, see `settings_custom.example.py`.
'''

# Hide error about using Google Recaptcha test keys
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
