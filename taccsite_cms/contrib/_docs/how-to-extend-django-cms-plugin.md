# How To Extend a `djangocms-___` Plugin

These example codes extend the [`djangocms-link` plugin](https://github.com/django-cms/djangocms-link/tree/3.0.0/djangocms_link).

`.../models.py`:

```python
from djangocms_link.models import AbstractLink

class Taccsite______(AbstractLink):
    """
    Components > "Article List" Model
    https://confluence.tacc.utexas.edu/x/OIAjCQ
    """
    # ___ = ___

    class Meta:
        abstract = False
```

`.../cms_plugins.py`:

```python
from djangocms_link.cms_plugins import LinkPlugin

from .models import ______Preview

class ______Plugin(LinkPlugin):
    module = 'TACC Site'
    model = Taccsite______
    name = _('______')
    render_template = 'static_article_preview.html'
    def get_render_template(self, context, instance, placeholder):
        return self.render_template

    fieldsets = [
        (_('Link'), {
            'fields': (
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
            'link_text': instance.name,
            'link_target': instance.target
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
