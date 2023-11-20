from django import template

register = template.Library()

@register.simple_tag
def blog_post_is_in_category(post=None, current_category=None, category_slug=''):
    """
    Custom Template Tag `blog_post_is_in_category`

    Use: Return (boolean) whether given blog post is in a given category.

    Load custom tag into template:
        {% load blog_post_is_in_category %}

    Template inline usage:
        {# (renders `True` or `False`) #}
        {% blog_post_is_in_category post 'include-me' %}

        {# (renders "A" or "B") #}
        {% blog_post_is_in_category post 'include-me' as should_include_post %}
        {% if should_include_post %} A {% else %} B {% endif %}

    Example:
        ../templates/djangocms_blog/post_list.html
    """
    is_in_category = False
    if not current_category.slug == category_slug:
        if post.categories.exists:
            for category in post.categories.all():
                if category.slug == category_slug:
                    is_in_category = True

    return is_in_category
