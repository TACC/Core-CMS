#!/usr/bin/env python
import os
import sys
import json

from django.conf import settings

from bin.suppress_stdout import suppress_stdout

# Support isolated reading of settings
sys.path.insert(0, os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taccsite_cms.settings")

# Create JSON
setting_names = ["THEME"]
settings_export = {}
# FAQ: The print() statements in settings.py would corrupt the JSON
with suppress_stdout():
    for setting_name in setting_names:
        settings_export[setting_name] = getattr(settings, setting_name)

# Write JSON
with open('taccsite_cms/settings.json', 'w', encoding='utf-8') as outfile:
    settings_json = json.dumps(settings_export, ensure_ascii=False, indent=2)
    outfile.write(settings_json + '\n')
