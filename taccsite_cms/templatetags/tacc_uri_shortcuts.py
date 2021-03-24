from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def site_uri(context):
    """
    Custom Template Tag `site_uri`

    Use: Access Site URI values in Templates.

    Load custom tag into template:
        {% load tacc_uri_shortcuts %}

    Template inline usage:
        {% site_uri.absolute_uri %}
        {% site_uri.scheme %}
        {% site_uri.host %}

    Example:
        <a href="{% site_uri.absolute_uri %}">site URL (on dev)</a>
            # <a href="https://localhost:8000">site URL (on dev)</a>
        <a href="{% site_uri.absolute_uri %}">site URL (on prod)</a>
            # <a href="https://brand.tacc.utexas.edu/">site URL (on dev)</a>
    """
    request = context['request']
    absolute_uri = request.build_absolute_uri('/')
    return {
        # NOTE: Alternative is `{{ request.scheme }}://{{ request.get_host }}`
        'absolute_uri': absolute_uri,

        # WARNING: These assume context of template matches site host.
        #          To avoid this, consider the Site module.
        # SEE: https://stackoverflow.com/a/897053
        # SEE: https://docs.djangoproject.com/en/3.1/ref/contrib/sites/
        # NOTE: Alternative is `{{ request.scheme }}`
        'scheme': request.scheme,
        # NOTE: Alternative is `{{ request.get_host }}`
        'host': request.get_host(),
    }
