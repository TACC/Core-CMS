from enum import Enum

# TODO: Consider adding 'GOOGLE' as an option
# SEE: https://github.com/TACC/tup-ui/blob/6eb9412/apps/tup-cms/src/taccsite_cms/settings_custom.py#L101
SearchEngines = Enum('SearchEngines', ['ELASTIC'])
