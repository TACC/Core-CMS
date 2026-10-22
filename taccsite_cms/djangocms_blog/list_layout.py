"""Resolve ``PORTAL_BLOG_LIST_LAYOUT`` for a djangocms_blog apphook namespace."""

from __future__ import annotations

import logging

from django.conf import settings

logger = logging.getLogger(f'portal.{__name__}')

BLOG_LIST_LAYOUT_CHOICES = frozenset({'grid', 'list'})
BLOG_LIST_LAYOUT_DEFAULT = 'list'


def portal_blog_list_layout(namespace: str | None = None) -> str:
    """
    Return ``list`` or ``grid`` for a blog apphook namespace.

    ``PORTAL_BLOG_LIST_LAYOUT`` may be a string (all blogs) or a dict keyed by
    ``BlogConfig.namespace`` / apphook ``application_namespace``.
    """
    configured = getattr(settings, 'PORTAL_BLOG_LIST_LAYOUT', BLOG_LIST_LAYOUT_DEFAULT)
    if isinstance(configured, str):
        layout = configured
    elif isinstance(configured, dict):
        if namespace and namespace in configured:
            layout = configured[namespace]
        else:
            layout = configured.get('default', BLOG_LIST_LAYOUT_DEFAULT)
    else:
        layout = BLOG_LIST_LAYOUT_DEFAULT
    if layout in BLOG_LIST_LAYOUT_CHOICES:
        return layout
    logger.warning(
        'PORTAL_BLOG_LIST_LAYOUT value %r is not valid (choices: %s); using %r.',
        layout,
        ', '.join(sorted(BLOG_LIST_LAYOUT_CHOICES)),
        BLOG_LIST_LAYOUT_DEFAULT,
    )
    return BLOG_LIST_LAYOUT_DEFAULT
