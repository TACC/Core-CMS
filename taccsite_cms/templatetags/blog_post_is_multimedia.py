from django import template

register = template.Library()

@register.simple_tag
def blog_post_is_multimedia(post=None):
    """
    Custom Template Tag `blog_post_is_multimedia`

    Use: Return (boolean) whether given blog post is a "Multimedia"-type post.

    Load custom tag into template:
        {% load blog_post_is_multimedia %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% blog_post_is_multimedia post %}

        {# (renders "A" or "B") #}
        {% blog_post_is_multimedia post as is_multimedia %}
        {% if is_multimedia %} A {% else %} B {% endif %}

    Example:
        ../templates/djangocms_blog/post_detail.html
    """
    if post.categories.exists:
        for cat in post.categories.all():
            if cat.slug == "multimedia":
                is_multimedia = True

    return is_multimedia
