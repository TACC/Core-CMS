# TODO: Consider using an Enum (and an Abstract Enum with `get_choices` and `get_classname` methods)

ORIENTATION_DICT = {
    'horizontal': {
        'classname':         'c-data-list--is-horz',
        'description':       'Horizontal (all data on one row)',
        'short_description': 'Horizontal',
    },
    'vertical': {
        'classname':         'c-data-list--is-vert',
        'description':       'Vertical (every label and value has its own row)',
        'short_description': 'Vertical',
    },
}

TYPE_STYLE_DICT = {
    'table': {
        'description':  'Table (e.g. Columns)',
        'short_description': 'Table',
    },
    'dlist': {
        'description':  'List (e.g. Glossary, Metadata)',
        'short_description': 'List',
    },
}

DENSITY_DICT = {
    'default': {
        'classname':         'c-data-list--is-wide',
        'description':       'Default (ample extra space)',
        'short_description': 'Default',
    },
    'compact': {
        'classname':         'c-data-list--is-narrow',
        'description':       'Compact (minimal extra space)',
        'short_description': 'Compact',
    },
}
