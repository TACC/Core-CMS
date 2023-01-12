from django import template

register = template.Library()

@register.simple_tag
def blog_post_is_multimedia(post=None, category_slug=''):
    """
    Custom Template Tag `blog_post_is_multimedia`

    Use: Return (boolean) whether given blog post is a "Multimedia"-type post.

    Load custom tag into template:
        {% load blog_post_is_multimedia %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% blog_post_is_multimedia post 'multimedia' %}

        {# (renders "A" or "B") #}
        {% blog_post_is_multimedia post 'multimedia' as is_multimedia %}
        {% if is_multimedia %} A {% else %} B {% endif %}

    Example:
        ../templates/djangocms_blog/post_detail.html
    """
    is_multimedia = False
    if post.categories.exists:
        for cat in post.categories.all():
            if cat.slug == category_slug:
                is_multimedia = True

    return is_multimedia
