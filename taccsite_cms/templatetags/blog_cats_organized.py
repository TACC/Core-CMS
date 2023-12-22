from django import template
from collections import OrderedDict

register = template.Library()

@register.filter
def filter_categories(categories):
    ordered_list = ['press-release', 'feature-story', 'multimedia', 'podcast']

    # Create a dictionary to store the indices of elements in the ordered list
    order_indices = {element: index for index, element in enumerate(ordered_list)}
    
    # Custom sorting function based on the indices in the ordered list
    def custom_sort(item):
        if item.slug in order_indices:
            return order_indices[item.slug]
        else:
            # For items not found in the ordered list, place them at the end
            return len(ordered_list)
    
    # Sort the categories list based on the custom sorting function
    sorted_categories = sorted(categories, key=custom_sort)

    return sorted_categories