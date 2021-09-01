# TODO: Consider using an Enum (and an Abstract Enum with `get_choices` method)
LAYOUT_DICT = {
    'cols-widest-2-even_width': {
        'classname':    'c-article-list--layout-a',
        'description':  '2 Equal-Width Columns',
    },
    'cols-widest-2-wide_narrow': {
        'classname':    'c-article-list--layout-b',
        'description':  '2 Columns: 1 Wide, 1 Narrow',
    },
    'cols-widest-2-narrow_wide': {
        'classname':    'c-article-list--layout-c',
        'description':  '2 Columns: 1 Narrow, 1 Wide',
    },
    'cols-widest-3-even_width': {
        'classname':    'c-article-list--layout-d',
        'description':  '3 Equal-Width Columns',
    },
    'rows-always-N-even_height': {
        'classname':    'c-article-list--layout-e'
                        '  ' + 'c-article-list--style-gapless',
        'description':  'Multiple Rows',
    },
}

STYLE_DICT = {
    'rows-divided': {
        'classname':    'c-article-list--style-divided',
        'description':  'Dividers Between Articles',
    },
    'cols-gapless': {
        'classname':    'c-article-list--style-gapless',
        'description':  'Remove Gaps Between Articles',
    },
}
