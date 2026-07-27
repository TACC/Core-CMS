from django import template
from django.conf import settings

PORTAL_BLOG_CATEGORY_ORDER = settings.PORTAL_BLOG_CATEGORY_ORDER
register = template.Library()

@register.filter
def sort_blog_categories(categories):

    # Create a dictionary to store the indices of elements in the ordered list
    order_indices = {element: index for index, element in enumerate(PORTAL_BLOG_CATEGORY_ORDER)}

    # Custom sorting function based on the indices in the ordered list
    def custom_sort(item):
        if item.slug in order_indices:
            return order_indices[item.slug]
        else:
            # For items not found in the ordered list, place them at the end
            return len(PORTAL_BLOG_CATEGORY_ORDER)

    # Sort the categories list based on the custom sorting function
    sorted_categories = sorted(categories, key=custom_sort)

    return sorted_categories
