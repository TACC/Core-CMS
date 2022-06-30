import re

from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def get_url_match(path, pattern):
    """
    Custom Template Filter `get_url_match`
    Use: Render string that matches given pattern from current page URL.
    Load custom filter into template:
        {% load get_url_match %}
    Template inline usage:
        {# given path '.../2019/...', does nothing #}
        {% if path|get_url_match:"/20\d\d/" %}
            {# condition evaluates to False #}
        {% endif %}
        {# given path '.../2020/...', does something #}
        {% if path|get_url_match:"/20\d\d/" %}
            {# condition evaluates to True #}
        {% endif %}
        {# given path '.../2021/...', prints complete match #}
        {% with year_path=path|get_url_match:"/20\d\d/" %}
            <pre>{{ year_path }}</pre> {# prints complete match #}
        {% endwith %}
        {# given path '.../2022/...', prints matched content #}
        {% with year_slug=path|get_url_match:"/(20\d\d)/" %}
            <pre>{{ year_slug }}</pre> {# prints match within the (…) #}
        {% endwith %}
    """
    result = re.search(pattern, path)

    if result:
        try:
            match = result.group(1)
        except IndexError:
            match = result[0]
    else:
        match = False

    return match
