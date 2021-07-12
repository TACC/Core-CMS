"""
.. module:: taccsite_sample.utils
   :synopsis: Utilities to process user name.
"""

def has_proper_name(user=None):
    """Whether user has enough data with which to form a proper name.

    :param user: Django user object

    :returns: True, False, or None (if unknown)
    :rtype: bool | None

    .. note::
        User must be authenticated or function will return None.
    """
    ret = None

    if user and user.is_authenticated:
        if user.first_name:
            ret = True
        else:
            ret = False

    return ret

def get_proper_name(user=None):
    """Get proper name of an authenticated user.

    :param user: Django user object (authenticated)

    :returns: Proper name of user
    :rtype: str | None

    .. note::
        If user is not authenticated, we do not know any name.
        If user has no first name, we give up (no name prefix logic).
    """
    name = None

    if has_proper_name(user):
        if bool(user.first_name):
            name = user.first_name
            if bool(user.last_name):
                name = name + ' ' + user.last_name

    return name
