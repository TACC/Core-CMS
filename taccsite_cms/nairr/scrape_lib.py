"""Fetch and extract HTML from nairrpilot.org for NAIRR migration."""

from __future__ import annotations

import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Comment

from taccsite_cms.nairr.page_registry import PLACEHOLDER_SENTINEL
from taccsite_cms.nairr.html_text import collapse_whitespace, polish_html_fragment

STRIP_SELECTORS = (
    '#resource_catalog_app',
    '#app',
    'script',
    'style',
    'noscript',
)

Joomla_PLACEHOLDER_RE = re.compile(
    r'COM_PILOT\w+|COM_\w+_DISPLAY',
    re.IGNORECASE,
)


def scrape_root(settings) -> Path:
    from django.conf import settings as django_settings

    root = getattr(django_settings, 'NAIRR_SCRAPE_ROOT', None)
    if not root:
        root = Path(django_settings.BASE_DIR) / 'scraped' / 'nairr'
    return Path(root)


def base_url(settings) -> str:
    from django.conf import settings as django_settings

    return getattr(
        django_settings,
        'NAIRR_SCRAPE_BASE_URL',
        'https://nairrpilot.org',
    ).rstrip('/')


def file_path_for_scrape_path(root: Path, scrape_path: str) -> Path:
    if scrape_path in ('', 'home'):
        return root / 'home.html'
    return root / f'{scrape_path}.html'


def fetch_html(scrape_path: str, *, base: str, session: requests.Session) -> str:
    if scrape_path in ('', 'home'):
        url = base + '/'
    else:
        url = urljoin(base + '/', scrape_path)
    response = session.get(url, timeout=60)
    response.raise_for_status()
    return response.text


def _remove_nodes(soup: BeautifulSoup) -> None:
    for selector in STRIP_SELECTORS:
        for node in soup.select(selector):
            node.decompose()
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()


def _extract_h1_fragment(soup: BeautifulSoup) -> str | None:
    """Page title in Joomla `content-header`, outside `contentpaneopen`."""
    h1 = soup.select_one('div.content-header h1')
    if not h1:
        h1 = soup.select_one('div.item-page div.content-header h1, main div.content-header h1')
    if not h1:
        return None
    text = collapse_whitespace(h1.get_text())
    if not text:
        return None
    return f'<h1>{text}</h1>'


def _prepend_h1_to_inner(inner: str, h1_fragment: str | None) -> str:
    if not h1_fragment or not inner:
        return inner or (h1_fragment or '')
    fragment = BeautifulSoup(inner, 'lxml')
    if fragment.find('h1'):
        return inner
    return f'{h1_fragment}\n{inner}'


def extract_article_html(document_html: str) -> str:
    soup = BeautifulSoup(document_html, 'lxml')
    _remove_nodes(soup)
    h1_fragment = _extract_h1_fragment(soup)
    pane = soup.select_one('div.contentpaneopen')
    if pane:
        inner = pane.decode_contents().strip()
    else:
        main = soup.select_one('main.page, main')
        inner = main.decode_contents().strip() if main else ''
    inner = _prepend_h1_to_inner(inner, h1_fragment)
    inner = polish_html_fragment(inner)
    return _finalize_extracted(inner)


def extract_home_html(document_html: str) -> str:
    soup = BeautifulSoup(document_html, 'lxml')
    _remove_nodes(soup)
    sweet = soup.select_one('div.sweet-home')
    if sweet:
        inner = sweet.decode_contents().strip()
    else:
        main = soup.select_one('main.page, main')
        inner = main.decode_contents().strip() if main else ''
    hero = soup.select_one('div.real-hero')
    parts = []
    if hero:
        parts.append(hero.decode_contents().strip())
    if inner:
        parts.append(inner)
    combined = '\n'.join(parts)
    combined = polish_html_fragment(combined)
    return _finalize_extracted(combined)


def _finalize_extracted(inner: str) -> str:
    text_only = BeautifulSoup(inner, 'lxml').get_text(' ', strip=True)
    if not text_only or len(text_only) < 20:
        return PLACEHOLDER_SENTINEL
    if Joomla_PLACEHOLDER_RE.search(text_only) and len(text_only) < 120:
        return PLACEHOLDER_SENTINEL
    return inner


def write_scrape_file(root: Path, scrape_path: str, html: str) -> Path:
    path = file_path_for_scrape_path(root, scrape_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')
    return path


def read_scrape_file(root: Path, scrape_path: str) -> str | None:
    path = file_path_for_scrape_path(root, scrape_path)
    if not path.is_file():
        return None
    return path.read_text(encoding='utf-8')


def is_placeholder(content: str | None) -> bool:
    if content is None:
        return True
    stripped = content.strip()
    return stripped == PLACEHOLDER_SENTINEL or not stripped


def scrape_one(
    scrape_path: str,
    *,
    root: Path,
    base: str,
    force: bool,
    crawl_delay: float,
) -> Path:
    out = file_path_for_scrape_path(root, scrape_path)
    if out.is_file() and not force:
        return out

    session = requests.Session()
    session.headers.update(
        {
            'User-Agent': 'TACC-NAIRR-CMS-Migration/1.0 (+local dev; respects robots crawl-delay)',
        }
    )
    html = fetch_html(scrape_path, base=base, session=session)
    if scrape_path in ('', 'home'):
        extracted = extract_home_html(html)
        write_path = write_scrape_file(root, 'home', extracted)
    else:
        extracted = extract_article_html(html)
        write_path = write_scrape_file(root, scrape_path, extracted)
    if crawl_delay:
        time.sleep(crawl_delay)
    return write_path
