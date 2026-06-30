"""Normalize text whitespace in scraped HTML fragments (headings, outer trim)."""

from __future__ import annotations

import re

from bs4 import BeautifulSoup

WHITESPACE_RE = re.compile(r'\s+')

HEADING_TAGS = ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')


def collapse_whitespace(text: str) -> str:
    return WHITESPACE_RE.sub(' ', text).strip()


def normalize_headings(root) -> None:
    """
    Collapse tabs/newlines in heading text (Joomla source indentation).

    Replaces heading contents with plain text; NAIRR page titles are not
    expected to rely on inline markup inside h1–h6.
    """
    for tag in root.find_all(HEADING_TAGS):
        text = collapse_whitespace(tag.get_text())
        if not text:
            tag.decompose()
            continue
        tag.clear()
        tag.append(text)


def prepare_article_html_chunk(html: str) -> str:
    """Trim imported fragment HTML before TextPlugin body."""
    return html.strip()


def polish_html_fragment(html: str) -> str:
    """Trim fragment edges and normalize heading text."""
    html = html.strip()
    if not html:
        return html
    soup = BeautifulSoup(f'<div data-nairr-fragment>{html}</div>', 'lxml')
    root = soup.select_one('div[data-nairr-fragment]')
    if not root:
        return html.strip()
    normalize_headings(root)
    return root.decode_contents().strip()


def trim_fragment_edges(html: str) -> str:
    return html.strip()


def _split_container_children(parent) -> list:
    """Direct child nodes with content (tags or non-empty text)."""
    from bs4 import NavigableString, Tag

    nodes = []
    for child in parent.children:
        if isinstance(child, NavigableString):
            if str(child).strip():
                nodes.append(child)
        elif isinstance(child, Tag):
            nodes.append(child)
    if len(nodes) == 1 and nodes[0].name == 'div':
        return _split_container_children(nodes[0])
    return nodes


def split_html_for_cms_text_plugins(html: str) -> list[str]:
    """
    Split article HTML into TextPlugin-sized chunks for Structure mode.

    - Each ``h1`` → one plugin
    - Each ``h2`` plus following content until the next ``h1``/``h2`` → one plugin
      (``h3``–``h6`` and body copy stay inside that ``h2`` chunk)
    - Leading content before the first heading → one plugin
    """
    html = html.strip()
    if not html:
        return []

    soup = BeautifulSoup(f'<div data-nairr-split>{html}</div>', 'lxml')
    root = soup.select_one('div[data-nairr-split]')
    if not root:
        return [html]

    nodes = _split_container_children(root)
    chunks: list[str] = []
    idx = 0
    while idx < len(nodes):
        node = nodes[idx]
        name = getattr(node, 'name', None)
        if name == 'h1':
            chunks.append(str(node))
            idx += 1
        elif name == 'h2':
            parts = [str(node)]
            idx += 1
            while idx < len(nodes):
                next_name = getattr(nodes[idx], 'name', None)
                if next_name in ('h1', 'h2'):
                    break
                parts.append(str(nodes[idx]))
                idx += 1
            chunks.append(''.join(parts))
        else:
            parts = []
            while idx < len(nodes):
                next_name = getattr(nodes[idx], 'name', None)
                if next_name in ('h1', 'h2'):
                    break
                parts.append(str(nodes[idx]))
                idx += 1
            if parts:
                chunks.append(''.join(parts))

    result = []
    for chunk in chunks:
        if BeautifulSoup(chunk, 'lxml').get_text(strip=True):
            result.append(chunk.strip())
    if not result:
        return [html]
    return result
