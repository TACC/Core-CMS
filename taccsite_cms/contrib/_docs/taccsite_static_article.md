# Static Article Plugins

## Intention

Support static addition of news articles that originate from a Core news site.

A [dynamic solution that pulls form the Core news site](https://github.com/TACC/Core-CMS/issues/69) is preferable.

But this is not available due to constrainst of architecture, time, or ability.

## Architecture

### (Currently) Add Image via Child Plugin Instead of Via Fields

Instead, the image fields should be in the plugin, __not__ via a child plugin, but a solution has not yet been implemented.

#### Hope for the Future

The `AbstractLink` model was successfully extended.

See:
    - [./how-to-extend-django-cms-plugin.md](./how-to-extend-django-cms-plugin.md)
    - [../taccsite_static_article_preview](../taccsite_static_article_preview)
    - [../taccsite_static_article_list](../taccsite_static_article_list)

#### Failed Attempt

1. Build model so it extends `AbstractPicture` from `djangocms-picture`.
2. Tweak model to sweep bugs under the rug.
3. Quit when he was unable to resolve the error,
    `TaccsiteStaticNewsArticlePreview has no field named 'cmsplugin_ptr_id'`
    upon saving a plugin instance.
4. Learn:
    - [one should not try to reduce `AbstractPicture`](https://stackoverflow.com/a/3674714/11817077)
    - [one should not subclass a subclass of `CMSPlugin`](https://github.com/django-cms/django-cms/blob/3.7.4/cms/models/pluginmodel.py#L104)

#### Abandoned Code

```python
from djangocms_picture.models import AbstractPicture

# To allow user to not set image
# FAQ: Emptying the clean() method avoids picture validation
# SEE: https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L278
def skip_image_validation():
    pass

class TaccsiteStaticNewsArticlePreview(AbstractPicture):
    #
    # …
    #

    # Remove error-prone attribute from parent class
    # FAQ: Avoid error when running `makemigrations`:
    #      "You are trying to add a non-nullable field 'cmsplugin_ptr' […]"
    # SEE: https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L212
    # SEE: https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L234
    cmsplugin_ptr = None

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        skip_image_validation()
```
