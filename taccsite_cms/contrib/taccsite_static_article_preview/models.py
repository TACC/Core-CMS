from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _

from django.db import models

from djangocms_attributes_field import fields

# Constants

MEDIA_SUPPORT_CHOICES = (
    ('nested', _('Nest a single Picture / Image plugin inside this plugin.')),
    # ('direct', _('Choose / Define an image directly within this plugin.')),
)

# Helpers

# This field lets us:
# - (for user) describe how to add media
# - (for code) identify instances added before media could be directly added
def create_media_support_field(blank=False):
    return models.CharField(
        choices=MEDIA_SUPPORT_CHOICES,
        verbose_name=_('How to Add an Image'),
        default=MEDIA_SUPPORT_CHOICES[0][0],
        blank=blank,
        max_length=255,
    )

def create_title_text_field(blank=True):
    return models.CharField(
        verbose_name=_('Title'),
        help_text='The title for the article.',
        blank=blank,
        max_length=50,
        default=''
    )

def create_abstract_text_field(blank=True):
    return models.TextField(
        verbose_name=_('Abstract'),
        help_text='A summary of the article',
        blank=blank,
        default=''
    )

def create_type_text_field(blank=True):
    return models.CharField(
        verbose_name=_('Type'),
        help_text='The type of the article, ex: "Science News", "Press Release" (manual entry).',
        blank=blank,
        max_length=50
    )

def create_author_text_field(blank=True):
    return models.CharField(
        verbose_name=_('Author'),
        help_text='The author of the article (manual entry).',
        blank=blank,
        max_length=50,
    )

def create_publish_date_field(blank=True):
    return models.DateField(
        verbose_name=_('Date Published'),
        help_text='The date the article was published (manual entry). Format: YYYY-MM-DD',
        blank=blank,
        null=True,
    )



# Models

class TaccsiteStaticNewsArticlePreview(CMSPlugin):
    media_support = create_media_support_field(blank=False)
    title_text = create_title_text_field(blank=False)
    abstract_text = create_abstract_text_field(blank=False)
    type_text = create_type_text_field()
    author_text = create_author_text_field()
    publish_date = create_publish_date_field()

    attributes = fields.AttributesField()
