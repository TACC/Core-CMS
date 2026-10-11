"""
Settings package:
- settings.py (core defaults; must remain in this package)
- overwrites/ (client override files; Docker-mountable)
- re-export main settings module (for backwards compatibility)
"""

from taccsite_cms.settings.settings import *
