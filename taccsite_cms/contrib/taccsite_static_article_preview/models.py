from cms.models.pluginmodel import CMSPlugin

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text
from django.db import models

from djangocms_link.models import AbstractLink

from taccsite_cms.contrib.helpers import clean_for_abstract_link



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

# Helpers: Field Creation
# FAQ: Allow fields to be shared between models without creating abstract model
# NOTE: What every model has could change depending on new page designs…

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

def create_publish_date_field(blank=True, help_text=None, verbose_name=None):
    return models.DateField(
        verbose_name=verbose_name
            if verbose_name
            else _('Date Published'),
        # Allocations repurposes this as date when submissions open
        help_text=help_text + ' Format: YYYY-MM-DD'
            if help_text
            else 'The date the article was published (manual entry).',
        blank=blank,
        null=True,
    )

def create_expiry_date_field(blank=True, help_text=None, verbose_name=None):
    return models.DateField(
        verbose_name=verbose_name
            if verbose_name
            else _('Date to Expire'),
        # Allocations repurposes this as date when submissions close
        help_text=help_text + ' Format: YYYY-MM-DD'
            if help_text
            else 'The date the article should no longer appear show (manual entry).',
        blank=blank,
        null=True,
    )



# Models

class TaccsiteStaticNewsArticlePreview(AbstractLink):
    media_support = create_media_support_field(blank=False)
    title_text = create_title_text_field(blank=False)
    abstract_text = create_abstract_text_field(blank=False)

    type_text = create_type_text_field()
    author_text = create_author_text_field()
    publish_date = create_publish_date_field()



    # Parent

    link_is_optional = True

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)

class TaccsiteStaticAllocsArticlePreview(AbstractLink):
    media_support = create_media_support_field(blank=False)
    title_text = create_title_text_field(blank=False)

    expiry_date = create_expiry_date_field(
        verbose_name='Submission End Date',
        help_text='The date after which submissions are not accepted (manual entry).'
    )
    publish_date = create_publish_date_field(
        verbose_name='Submission Start Date',
        help_text='The date after which submissions are accepted (manual entry).'
    )



    # Parent

    link_is_optional = True

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)

class TaccsiteStaticDocsArticlePreview(AbstractLink):
    title_text = create_title_text_field(blank=False)
    abstract_text = create_abstract_text_field(blank=False)



    # Parent

    link_is_optional = True

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)

class TaccsiteStaticEventsArticlePreview(AbstractLink):
    title_text = create_title_text_field(blank=False)
    abstract_text = create_abstract_text_field(blank=False)

    expiry_date = create_expiry_date_field(
        verbose_name='Event End Date',
        help_text='The date upon which the event starts (manual entry).'
    )
    publish_date = create_publish_date_field(
        verbose_name='Event Start Date',
        help_text='The date after which the event ends (manual entry).'
    )



    # Parent

    link_is_optional = True

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)

        # If user provided link text, then require link
        if not self.publish_date and not self.expiry_date:
            end_date_name = force_text(
                self._meta.get_field('expiry_date').verbose_name )
            start_date_name = force_text(
                self._meta.get_field('publish_date').verbose_name )
            raise ValidationError(
                _('Provide either a %(start_date)s or an %(end_date)s.') % {
                    'start_date': start_date_name, 'end_date': end_date_name
                },
                code='invalid'
            )
