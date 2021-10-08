from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'dev'

base_settings = [
    optional('secrets.py'),
    optional('settings_custom.py'),
    optional('settings_custom.{}.py'.format(ENV)),
    optional('settings_local.py'),
]

# Include settings:
include(*base_settings)
