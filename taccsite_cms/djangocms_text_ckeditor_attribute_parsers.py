"""Allowlists for djangocms-text-ckeditor HTML sanitization."""

from djangocms_text_ckeditor.sanitizer import AllowTokenParser


class AriaAttributeParser(AllowTokenParser):
    """Allow WAI-ARIA attributes (html5lib allowlist omits aria-* by default)."""

    def parse(self, attribute, val):
        return attribute.startswith('aria-')
