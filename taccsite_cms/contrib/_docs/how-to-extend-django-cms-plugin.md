# How To Extend a `djangocms-___` Plugin

These example codes extend the [`djangocms-link` plugin](https://github.com/django-cms/djangocms-link/tree/3.0.0/djangocms_link).

`.../models.py`:

```python
from djangocms_link.models import AbstractLink

from taccsite_cms.contrib.helpers import clean_for_abstract_link

class Taccsite______(AbstractLink):
    """
    Components > "Article List" Model
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    # ...



    # Parent

    link_is_optional = True # or False

    class Meta:
        abstract = False

    # Validate
    def clean(self):
        clean_for_abstract_link(__class__, self)
```

`.../cms_plugins.py`:

```python
from djangocms_link.cms_plugins import LinkPlugin

from .models import ______Preview

class ______Plugin(LinkPlugin):
    # ...
    render_template = 'static_article_preview.html'
    def get_render_template(self, context, instance, placeholder):
        return self.render_template

    fieldsets = [
        # ...
        (_('Link'), {
            'fields': (
                # 'name', # to use LinkPlugin "Display name"
                ('external_link', 'internal_link'),
                ('anchor', 'target'),
            )
        }),
    ]

    # Render
    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'link_url': instance.get_link(),
            'link_target': instance.target
            # 'link_text': instance.name, # to use LinkPlugin "Display name"
        })
        return context
```

`.../templates/______.py`:

```handlebars

<a class="______" href="{{ link_url }}"
  {% if link_target %}target="{{ link_target }}"{% endif %}>
  <span>{{ link_text }}
</a>
```
