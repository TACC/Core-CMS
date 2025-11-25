from django import template

register = template.Library()

@register.simple_tag
def blog_post_has_category(post=None, category_slug=''):
    """
    Custom Template Tag `blog_post_has_category`

    Use: Return (boolean) whether given blog post has a specific category.

    Load custom tag into template:
        {% load blog_post_has_category %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% blog_post_has_category post 'some_category' %}

        {# (renders "A" or "B") #}
        {% blog_post_has_category post 'some_category' as is_some_category %}
        {% if is_some_category %} A {% else %} B {% endif %}

    Example:
        ../templates/djangocms_blog/post_detail.html
    """
    has_category = False
    if post.categories.exists:
        for cat in post.categories.all():
            if cat.slug == category_slug:
                has_category = True

    return has_category
