from django import template

register = template.Library()

@register.simple_tag
def blog_post_has_tag(post=None, tag_slug=''):
    """
    Custom Template Tag `blog_post_has_tag`

    Use: Return (boolean) whether given blog post has a specific tag.
    Load custom tag into template:
        {% load blog_post_has_tag %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% blog_post_has_tag post 'some_tag' %}
        {# (renders "A" or "B") #}
        {% blog_post_has_tag post 'some_tag' as is_some_tag %}
        {% if is_some_tag %} A {% else %} B {% endif %}

    Example:
        ../templates/djangocms_blog/post_detail.html
    """
    has_tag = False
    if post.tags.exists:
        for tag in post.tags.all():
            if tag.slug == tag_slug:
                has_tag = True

    return has_tag
