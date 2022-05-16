from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter(takes_context=True)
def get_url_match(context, pattern):
    """
    Custom Template Filter `get_url_match`

    Use: Render string that matches given pattern from current page URL.

    Load custom filter into template:
        {% load get_url_match %}

    Template inline usage:
        {# given path '.../2020/...' (does something) #}
        {% if path|get_url_match:"/20\d\d/" %}
            # do something
        {% endif %}

        {# given path '.../1921/...' (does nothing) #}
        {% if path|get_url_match:"/20\d\d/" %}
            # do something
        {% endif %}
    """
    request = context['request']
    req_uri = request.build_absolute_uri('/')
    req_url = urlparse(req_uri)
    req_path = req.path

    match = re.search(pattern, req_path)
    if match:
        return match[0]
    else:
        return False
