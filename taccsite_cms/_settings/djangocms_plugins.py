"""Configure CMS plugins"""

import os

from django.utils.translation import gettext_lazy as _

########################
# ../settings.py
########################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

########################
# CKEDITOR
# https://github.com/django-cms/djangocms-text-ckeditor
########################

CKEDITOR_SETTINGS = {
    'autoParagraph': False,
    'stylesSet': 'default:/static/js/addons/ckeditor.wysiwyg.js',
    'contentsCss': ['/static/djangocms_text_ckeditor/ckeditor/contents.css'],
}

########################
# DJANGOCMS_PICTURE
# https://github.com/django-cms/djangocms-picture
########################

DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS = [
    576, 768, 992, 1200, 1400, 1680, 1920
]
DJANGOCMS_PICTURE_RATIO = 1.618
DJANGOCMS_PICTURE_ALIGN = [
    ('left', _('Align left')),
    ('right', _('Align right')),
    ('center', _('Align center')),
]
DJANGOCMS_PICTURE_TEMPLATES = [
    ('no_link_to_ext_image', _('Do not link to external image')),
    ('header_logo', _('Header logo')),
]

########################
# DJANGOCMS_AUDIO
# https://github.com/django-cms/djangocms-audio
########################

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']

########################
# DJANGOCMS_VIDEO
# https://github.com/django-cms/djangocms-video
########################

DJANGOCMS_VIDEO_TEMPLATES = [
    ('responsive-auto', _('Responsive - Automatic')),
    ('responsive-16by9', _('Responsive - 16 by 9')),
    ('responsive-4by3', _('Responsive - 4 by 3')),
    ('responsive-1by1', _('Responsive - 1 by 1')),
    ('responsive-21by9', _('Responsive - 21 by 9')),
]

########################
# DJANGOCMS_BOOTSTRAP
# https://github.com/django-cms/djangocms-bootstrap4
########################

DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = [
    ('col', _('Column')),
    ('col col-dark', _('Dark column')),
    ('col col-muted', _('Muted column')),
    ('w-100', _('Break')),
    ('', _('Empty'))
]

DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = [
    ('container', _('Container')),
    ('container-fluid', _('Fluid container')),
    ('o-section', _('Section')),
    ('_', _('None')),
    (_('Container'), (
        (
            'container  o-section',
            _('Container + Section (transparent / margin)')
        ),
        (
            'container  o-section o-section--style-light',
            _('Container + Light section')
        ),
        (
            'container  o-section o-section--style-muted',
            _('Container + Muted section')
        ),
        (
            'container  o-section o-section--style-dark',
            _('Container + Dark section')
        ),
    )),
    (_('Fluid container'), (
        (
            'container-fluid  o-section',
            _('Fluid container + Section (transparent / margin)')
        ),
        (
            'container-fluid  o-section o-section--style-light',
            _('Fluid container + Light section')
        ),
        (
            'container-fluid  o-section o-section--style-muted',
            _('Fluid container + Muted section')
        ),
        (
            'container-fluid  o-section o-section--style-dark',
            _('Fluid container + Dark section')
        ),
    )),
    (_('Section only'), (
        (
            'o-section o-section--style-light',
            _('Light section')
        ),
        (
            'o-section o-section--style-muted',
            _('Muted section')
        ),
        (
            'o-section o-section--style-dark',
            _('Dark section')
        ),
    )),
]

DJANGOCMS_BOOTSTRAP4_COLOR_STYLE_CHOICES = (
    ('primary', _('Primary')),
    ('secondary', _('Secondary')),
    # Disable for bootstrap4_link
    # WARNING: Might still want for bootstrap4_alerts
    # ('success', _('Success')),
    # ('danger', _('Danger')),
    # ('warning', _('Warning')),
    # ('info', _('Info')),
    ('light', _('Light')),
    ('dark', _('Dark')),
)

########################
# DJANGOCMS_STYLE
# https://github.com/django-cms/djangocms-style
########################

DJANGOCMS_STYLE_CHOICES = [
    'card',
    'card--plain',
    'card--standard',
    'card--image-top',
    'card--image-bottom',
    'card--image-right',
    'card--image-left',
    'section',
    'section--light',
    'section--muted',
    'section--dark',
    'o-section',
    'o-section o-section--style-light',
    'o-section o-section--style-muted',
    'o-section o-section--style-dark',
    'c-callout',
    'c-recognition c-recognition--style-light',
    'c-recognition c-recognition--style-dark',
    'c-nav', # bare-bones instance
    'c-nav c-nav--boxed',
]

DJANGOCMS_STYLE_TAGS = [
    # Even though <div> is often NOT the most semantic choice;
    # CMS editor may neglect tag, any other tag could be inaccurate,
    # and <div> is never inaccurate; so <div> is placed first 😞
    # RFE: Support automatically choosing tag based on class name
    # SEE: https://github.com/TACC/Core-CMS/pull/432
    'div',
    # Ordered by expected usage
    'section', 'article', 'header', 'footer', 'aside', 'nav',
    # Not expected but not unreasonable
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]

########################
# DJANGOCMS_ICON
# https://github.com/django-cms/djangocms-icon
########################

ICON_PATH = os.path.join('taccsite_cms', 'static', 'site_cms', 'img', 'icons')

LOGO_ICONFILE = os.path.join(BASE_DIR, ICON_PATH, 'logos.json')
with open(LOGO_ICONFILE, 'r') as f:
    LOGO_ICONS = f.read()

CORTAL_ICONFILE = os.path.join(BASE_DIR, ICON_PATH, 'cortal.json')
with open(CORTAL_ICONFILE, 'r') as f:
    CORTAL_ICONS = f.read()

DJANGOCMS_ICON_SETS = [
    # IMPORTANT: Each set must have same props, even if value is empty
    # WARNING: Values in icon sets are not cleared when user changes set
    # IMPORTANT: Load 'icon' set last, or selected SVG may be unselected on edit
    # https://github.com/django-cms/djangocms-icon/issues/9
    (LOGO_ICONS, '', _('Logo SVGs')),
    (CORTAL_ICONS, 'icon', _('TACC "Cortal" Icons')),
]
