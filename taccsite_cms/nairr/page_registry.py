"""
NAIRR page tree for create_nairr_pages / scrape_nairr_pages.

scrape_path: path on nairrpilot.org (no leading slash).
pattern: import layout — see NAIRR CMS Clone plan.
"""

from dataclasses import dataclass
from typing import Optional

PLACEHOLDER_SENTINEL = '<!-- placeholder -->'


@dataclass(frozen=True)
class PageSpec:
    slug: str
    title: str
    template: str
    scrape_path: str
    pattern: str
    parent_slug: Optional[str] = None
    in_navigation: bool = True


SECTION_PARENTS = {
    'about': 'About',
    'opportunities': 'Opportunities',
    'projects': 'Projects',
    'news': 'News/Events',
    'help': 'Learn/Get Help',
}


def reverse_id_for_slug(slug: str) -> str:
    key = slug.strip('/') or 'home'
    return 'nairr-' + key.replace('/', '-')


# Order: parents before children where parent_slug is set.
PAGE_SPECS = [
    PageSpec('', 'NAIRR Pilot', 'fullwidth.html', '', 'home', in_navigation=True),
    PageSpec('getting-started', 'Get Started', 'standard.html', 'getting-started', 'getting_started'),
    PageSpec('about', 'About', 'standard.html', '', 'section_parent'),
    PageSpec('about/overview', 'Overview', 'standard.html', 'about/overview', 'article', parent_slug='about'),
    PageSpec('about/secure', 'NAIRR Secure', 'standard.html', 'about/secure', 'article', parent_slug='about'),
    PageSpec('opportunities', 'Opportunities', 'standard.html', '', 'section_parent'),
    PageSpec(
        'opportunities/startup-project',
        'Start-Up Project',
        'standard.html',
        'opportunities/startup-project',
        'article',
        parent_slug='opportunities',
    ),
    PageSpec(
        'opportunities/allocations',
        'Research Resources',
        'standard.html',
        'opportunities/allocations',
        'sidebar_article',
        parent_slug='opportunities',
    ),
    PageSpec(
        'opportunities/education-call',
        'Educational Resources',
        'standard.html',
        'opportunities/education-call',
        'article',
        parent_slug='opportunities',
    ),
    PageSpec(
        'opportunities/deep-partnerships',
        'Deep Partnerships',
        'standard.html',
        'opportunities/deep-partnerships',
        'sidebar_article',
        parent_slug='opportunities',
    ),
    PageSpec(
        'pilotresources',
        'Open Data, Models, and More',
        'standard.html',
        'pilotresources',
        'article',
    ),
    PageSpec(
        'opportunities/how-review-matching-works',
        'How Request Review & Matching Works',
        'standard.html',
        'opportunities/how-review-matching-works',
        'article',
        parent_slug='opportunities',
    ),
    PageSpec(
        'opportunities/speaker-request',
        'Request a NAIRR Pilot Speaker',
        'standard.html',
        'opportunities/speaker-request',
        'article',
        parent_slug='opportunities',
    ),
    PageSpec('projects', 'Projects', 'standard.html', '', 'section_parent'),
    PageSpec(
        'projects/awarded',
        'Resource Allocations',
        'standard.html',
        'projects/awarded',
        'empty',
        parent_slug='projects',
    ),
    PageSpec(
        'projects/demo',
        'Demonstration Projects',
        'standard.html',
        'projects/demo',
        'article',
        parent_slug='projects',
    ),
    PageSpec(
        'projects/expansion',
        'Expansion Projects',
        'standard.html',
        'projects/expansion',
        'article',
        parent_slug='projects',
    ),
    PageSpec('map', 'Projects Map', 'fullwidth.html', 'map', 'empty'),
    PageSpec(
        'projects/sandbox',
        'Sandbox Projects',
        'standard.html',
        'projects/sandbox',
        'article',
        parent_slug='projects',
    ),
    PageSpec(
        'projects/highlights',
        'Project Highlights',
        'standard.html',
        'projects/highlights',
        'empty',
        parent_slug='projects',
    ),
    PageSpec('news', 'News/Events', 'standard.html', '', 'section_parent'),
    PageSpec(
        'news/news',
        'News',
        'standard.html',
        'news/news',
        'blog',
        parent_slug='news',
    ),
    PageSpec(
        'news/newsletters',
        'Newsletters',
        'standard.html',
        'news/newsletters',
        'blog',
        parent_slug='news',
    ),
    PageSpec(
        'news/events',
        'Events and Training',
        'standard.html',
        'news/events',
        'article',
        parent_slug='news',
    ),
    PageSpec(
        'news/community-workshops',
        'Community Workshops',
        'standard.html',
        'news/community-workshops',
        'article',
        parent_slug='news',
    ),
    PageSpec(
        'news/video',
        'Videos Archive',
        'standard.html',
        'news/video',
        'article',
        parent_slug='news',
    ),
    PageSpec('help', 'Learn/Get Help', 'standard.html', '', 'section_parent'),
    PageSpec('help/faq', 'Frequently Asked Questions', 'standard.html', 'help/faq', 'faq', parent_slug='help'),
    PageSpec(
        'help/videos',
        'Videos Archive',
        'standard.html',
        'help/videos',
        'article',
        parent_slug='help',
    ),
    PageSpec(
        'help/presentations',
        'Getting Started Presentations',
        'standard.html',
        'help/presentations',
        'article',
        parent_slug='help',
    ),
    PageSpec(
        'help/office-hours',
        'Office Hours',
        'standard.html',
        'help/office-hours',
        'article',
        parent_slug='help',
    ),
]


def scrape_targets():
    """Unique scrape paths for scrape_nairr_pages --all."""
    seen = set()
    for spec in PAGE_SPECS:
        if spec.pattern in ('section_parent', 'home'):
            continue
        path = spec.scrape_path
        if path not in seen:
            seen.add(path)
            yield path


def spec_by_slug(slug: str) -> Optional[PageSpec]:
    normalized = slug.strip('/')
    if normalized == 'home':
        normalized = ''
    for spec in PAGE_SPECS:
        if spec.slug == normalized:
            return spec
    return None


def expand_specs_with_ancestors(specs: list[PageSpec]) -> list[PageSpec]:
    """Ensure section parents exist when importing a single child (e.g. about/overview)."""
    by_slug = {s.slug: s for s in PAGE_SPECS}
    ordered: list[PageSpec] = []
    seen: set[str] = set()

    def visit(slug: str) -> None:
        if slug in seen:
            return
        spec = by_slug.get(slug)
        if not spec:
            return
        if spec.parent_slug:
            visit(spec.parent_slug)
        ordered.append(spec)
        seen.add(slug)

    for spec in specs:
        visit(spec.slug)
    return ordered
