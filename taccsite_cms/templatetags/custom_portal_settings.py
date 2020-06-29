from django import template

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]


"""
Template Tag Usage

Setting Value:
settings_values = [['a','b','c'], ['d','e','f']]

Template Usage:
{{ settings_values|index:x|index:y }}

-- to get my_list[x][y]
-- works with for loops: {{ my_list|index:forloop.counter0 }}
"""
