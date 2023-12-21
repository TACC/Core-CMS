from django import template
from collections import OrderedDict

register = template.Library()

@register.filter
def filter_categories(categories):
    # Create two different arrays of information in the order requested
    allowed_slugs_1 = ['press-release', 'feature-story']
    allowed_slugs_2 = ['multimedia', 'podcast']

    # Create a dictionary that labels each list in the order we would like
    # OrderedDict will keep this in place for us
    filtered_categories = OrderedDict([
        ('allowed_1', []),
        ('allowed_2', []),
        ('other', [])
    ])

    # Iterate through each category and enter it into to the respective list
    for category in categories:
        if category.slug in allowed_slugs_1:
            filtered_categories['allowed_1'].append(category)
        elif category.slug in allowed_slugs_2:
            filtered_categories['allowed_2'].append(category)
        else:
            filtered_categories['other'].append(category)

    # Create a new list where we will add in each list
    concatenated_list = []
    for key in filtered_categories:
        concatenated_list.extend(filtered_categories[key])

    return concatenated_list