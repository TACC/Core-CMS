from django import template

register = template.Library()

@register.simple_tag
def blog_post_is_show_abstract(post=None, tag_slug=''):
    """
    Custom Template Tag `blog_post_is_show_abstract`

    Use: Return (boolean) whether given blog post is a "show_abstract" post.

    Load custom tag into template:
        {% load blog_post_is_show_abstract %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% blog_post_is_show_abstract post 'show_abstract' %}

        {# (renders "A" or "B") #}
        {% blog_post_is_show_abstract post 'show_abstract' as is_show_abstract %}
        {% if is_show_abstract %} A {% else %} B {% endif %}

    Example:
        ../templates/djangocms_blog/post_detail.html
    """
    is_show_abstract = False
    if post.tags.exists:
        for tag in post.tags.all():
            if tag.slug == tag_slug:
                is_show_abstract = True

    return is_show_abstract
