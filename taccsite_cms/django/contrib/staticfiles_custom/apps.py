# FAQ: Avoid `TemplateSyntaxError` "'staticfiles' is not a registered tag library."
# SEE: https://docs.djangoproject.com/en/2.2/ref/applications/#for-application-authors

from django.contrib.staticfiles.apps import StaticFilesConfig

# Make `python manage.py collectstatic` ignore `src/` files
# FAQ: Do not allow developers to load source files as static files
class TaccStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = [
        # Original values
        # SEE: https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/#customizing-the-ignored-pattern-list
        'CVS', '.*', '*~',
        # Added by TACC
        # WARNING: Ignores these from non-TACC static's also
        'README.md', "*src/*.css"
    ]
