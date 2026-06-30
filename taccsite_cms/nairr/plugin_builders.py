"""Build django CMS plugins for NAIRR imported pages."""

from __future__ import annotations

from bs4 import BeautifulSoup

from cms.api import add_plugin

from taccsite_cms.nairr.html_text import (
    collapse_whitespace,
    prepare_article_html_chunk,
    split_html_for_cms_text_plugins,
)

from djangocms_bootstrap4.contrib.bootstrap4_grid.cms_plugins import (
    Bootstrap4GridColumnPlugin,
    Bootstrap4GridContainerPlugin,
    Bootstrap4GridRowPlugin,
)
from djangocms_style.cms_plugins import StylePlugin
from djangocms_text_ckeditor.cms_plugins import TextPlugin

MUTED_SECTION = 'container  o-section o-section--style-muted'
# DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS (admin label “Section”)
GRID_CONTAINER_TYPE_SECTION = 'o-section'
# DJANGOCMS_STYLE_CHOICES
STYLE_CLASS_NAME_SECTION = 'section'


class ContentBuilder:
    def __init__(self, placeholder, language):
        self.placeholder = placeholder
        self.language = language

    def add_text(self, parent, html: str):
        return add_plugin(
            self.placeholder,
            TextPlugin,
            self.language,
            target=parent,
            body=html,
        )

    def add_style(self, parent, class_name: str, tag_type='div'):
        return add_plugin(
            self.placeholder,
            StylePlugin,
            self.language,
            target=parent,
            class_name=class_name,
            tag_type=tag_type,
        )

    def add_container(self, parent, container_type=MUTED_SECTION, tag_type='div'):
        return add_plugin(
            self.placeholder,
            Bootstrap4GridContainerPlugin,
            self.language,
            target=parent,
            container_type=container_type,
            tag_type=tag_type,
        )

    def add_row(self, parent):
        return add_plugin(
            self.placeholder,
            Bootstrap4GridRowPlugin,
            self.language,
            target=parent,
            vertical_alignment='',
            horizontal_alignment='',
        )

    def add_column(self, parent, xs_col=12):
        return add_plugin(
            self.placeholder,
            Bootstrap4GridColumnPlugin,
            self.language,
            target=parent,
            column_type='col',
            column_alignment='',
            xs_col=xs_col,
        )

    def add_card_standard_text(self, parent, html: str):
        card = self.add_style(parent, 'card--standard', tag_type='article')
        self.add_text(card, html)
        return card

    def add_card_plain_text(self, parent, html: str):
        card = self.add_style(parent, 'card--plain', tag_type='article')
        self.add_text(card, html)
        return card

    def add_card_image_top_text(self, parent, html: str):
        card = self.add_style(parent, 'card--image-top', tag_type='article')
        self.add_text(card, html)
        return card


def extract_announcement_banners(html: str) -> list[str]:
    soup = BeautifulSoup(html, 'lxml')
    banners = []
    for node in soup.select('div.announcement-banner'):
        banners.append(node.decode_contents().strip())
        node.decompose()
    return banners


def dedupe_banner_html(banners: list[str]) -> str | None:
    if not banners:
        return None
    seen = set()
    for body in banners:
        key = BeautifulSoup(body, 'lxml').get_text(' ', strip=True)
        if key and key not in seen:
            seen.add(key)
            return body
    return banners[0]


def _h1_markup(h1) -> str | None:
    text = collapse_whitespace(h1.get_text())
    if not text:
        return None
    return f'<h1>{text}</h1>'


def _emit_leading_h1(builder: ContentBuilder, parent, soup: BeautifulSoup) -> None:
    """Page `<h1>` from scrape (before body sections)."""
    h1 = soup.find('h1')
    if not h1:
        return
    parent_classes = h1.find_parent('div', class_=True)
    if parent_classes and parent_classes.get('class'):
        if any('subsection' in c for c in parent_classes['class']):
            return
    markup = _h1_markup(h1)
    if not markup:
        h1.decompose()
        return
    container = builder.add_container(
        parent,
        container_type=GRID_CONTAINER_TYPE_SECTION,
        tag_type='section',
    )
    builder.add_text(container, prepare_article_html_chunk(markup))
    h1.decompose()


def _chunk_leading_tag(chunk: str) -> str | None:
    soup = BeautifulSoup(f'<div data-nairr-lead>{chunk}</div>', 'lxml')
    root = soup.select_one('div[data-nairr-lead]')
    if not root:
        return None
    for node in root.children:
        name = getattr(node, 'name', None)
        if name:
            return name
    return None


def _emit_overview_operations_teams(builder: ContentBuilder, parent, chunk: str) -> None:
    """Overview: h2 + lead in a section; teams in a two-column row like Joomla ``div.teams``."""
    soup = BeautifulSoup(f'<div data-nairr-teams>{chunk}</div>', 'lxml')
    root = soup.select_one('div[data-nairr-teams]')
    if not root:
        return
    teams = root.select_one('div.teams')
    section = builder.add_style(parent, STYLE_CLASS_NAME_SECTION, tag_type='section')
    if teams:
        before_parts: list[str] = []
        for child in root.children:
            if getattr(child, 'name', None) == 'div' and child.get('class') and 'teams' in child.get(
                'class', []
            ):
                break
            before_parts.append(str(child))
        intro = prepare_article_html_chunk(''.join(before_parts))
        if intro:
            builder.add_text(section, intro)
        column_divs = [
            child
            for child in teams.children
            if getattr(child, 'name', None) == 'div'
        ]
        if column_divs:
            row = builder.add_row(section)
            xs_col = 12 // len(column_divs)
            for column_div in column_divs:
                col = builder.add_column(row, xs_col=xs_col)
                for team in column_div.select('div.team'):
                    inner = prepare_article_html_chunk(team.decode_contents().strip())
                    if inner:
                        builder.add_card_plain_text(col, inner)
        else:
            for team in teams.select('div.team'):
                inner = prepare_article_html_chunk(team.decode_contents().strip())
                if inner:
                    builder.add_card_plain_text(section, inner)
    else:
        builder.add_text(section, prepare_article_html_chunk(chunk))


def add_article_text_plugins(
    builder: ContentBuilder,
    parent,
    html: str,
    *,
    page_slug: str | None = None,
) -> None:
    """Text plugins in section/container wrappers; h1 container, h2+ in Style section."""
    if not html or not html.strip():
        return
    for chunk in split_html_for_cms_text_plugins(html):
        chunk = prepare_article_html_chunk(chunk)
        if not chunk:
            continue
        lead = _chunk_leading_tag(chunk)
        if page_slug == 'about/overview' and lead == 'h2':
            soup_bit = BeautifulSoup(chunk, 'lxml')
            h2 = soup_bit.find('h2')
            title = collapse_whitespace(h2.get_text()) if h2 else ''
            if title == 'NAIRR Pilot Operations Teams':
                _emit_overview_operations_teams(builder, parent, chunk)
                continue
        if lead == 'h1':
            container = builder.add_container(
                parent,
                container_type=GRID_CONTAINER_TYPE_SECTION,
                tag_type='section',
            )
            builder.add_text(container, chunk)
        elif lead == 'h2':
            section = builder.add_style(parent, STYLE_CLASS_NAME_SECTION, tag_type='section')
            builder.add_text(section, chunk)
        else:
            builder.add_text(parent, chunk)


def build_article(builder: ContentBuilder, parent, html: str, *, page_slug: str | None = None) -> None:
    add_article_text_plugins(builder, parent, html, page_slug=page_slug)


def build_sidebar_article(
    builder: ContentBuilder,
    parent,
    html: str,
    *,
    page_slug: str | None = None,
) -> None:
    soup = BeautifulSoup(html, 'lxml')
    banners = []
    for node in soup.select('div.announcement-banner'):
        banners.append(node.decode_contents().strip())
        node.decompose()
    body_html = soup.decode_contents().strip()
    banner_html = dedupe_banner_html(banners)

    row = builder.add_row(parent)
    main_col = builder.add_column(row, xs_col=8)
    if body_html:
        add_article_text_plugins(builder, main_col, body_html, page_slug=page_slug)
    if banner_html:
        side_col = builder.add_column(row, xs_col=4)
        builder.add_card_standard_text(side_col, banner_html)


def build_faq(builder: ContentBuilder, parent, html: str) -> None:
    soup = BeautifulSoup(html, 'lxml')
    _emit_leading_h1(builder, parent, soup)
    banners = []
    for node in soup.select('div.announcement-banner'):
        banners.append(node.decode_contents().strip())
        node.decompose()
    banner_html = dedupe_banner_html(banners)

    if banner_html:
        top_row = builder.add_row(parent)
        builder.add_column(top_row, xs_col=8)
        side = builder.add_column(top_row, xs_col=4)
        builder.add_card_standard_text(side, banner_html)

    for heading in soup.find_all('h2'):
        category_title = heading.get_text(' ', strip=True)
        if not category_title:
            continue
        accordion = heading.find_next_sibling('div', class_=lambda c: c and 'hz-accordion' in c)
        if not accordion:
            continue
        details_blocks = []
        for trigger in accordion.select('button.accordion-trigger'):
            question = trigger.get_text(' ', strip=True)
            panel = trigger.find_next_sibling('div', class_='accordion-panel')
            answer_html = panel.decode_contents().strip() if panel else ''
            details_blocks.append(
                f'<details><summary>{question}</summary>{answer_html}</details>'
            )
        row = builder.add_row(parent)
        head_col = builder.add_column(row, xs_col=4)
        class_names = heading.get('class') or []
        if class_names:
            class_attr = ' '.join(class_names)
            h2_html = f'<h2 class="{class_attr}">{category_title}</h2>'
        else:
            h2_html = f'<h2 class="as-h3">{category_title}</h2>'
        builder.add_text(head_col, h2_html)
        body_col = builder.add_column(row, xs_col=8)
        builder.add_text(body_col, '\n'.join(details_blocks))


def _tile_html_from_element(element) -> str:
    return element.decode_contents().strip()


def build_home_from_scrape(builder: ContentBuilder, parent, html: str) -> None:
    soup = BeautifulSoup(html, 'lxml')

    hero = soup.select_one('div.real-hero')
    if hero:
        builder.add_text(
            parent,
            hero.decode_contents().strip(),
        )

    stats = soup.select_one('section.stats')
    if stats:
        builder.add_text(parent, stats.decode_contents().strip())

    for section in soup.select('section.section.shaded.pilot.opportunities, section.section.shaded.news.pilot'):
        container = builder.add_container(parent)
        row = builder.add_row(container)
        for item in section.select('div.split.items-grid > div, div.items-grid > div'):
            inner = _tile_html_from_element(item)
            if not inner or len(BeautifulSoup(inner, 'lxml').get_text(strip=True)) < 5:
                continue
            col = builder.add_column(row, xs_col=12)
            builder.add_card_standard_text(col, inner)

    highlights = soup.select_one('section.section.projects-highlights')
    if highlights:
        container = builder.add_container(parent, container_type='container')
        row = builder.add_row(container)
        for link in highlights.select('div.news-highlights a'):
            tile_html = link.decode_contents().strip()
            if not tile_html:
                continue
            href = link.get('href', '')
            if href and href not in tile_html:
                tile_html = f'<a href="{href}">{tile_html}</a>'
            col = builder.add_column(row, xs_col=12)
            builder.add_card_image_top_text(col, tile_html)

    happenings = soup.select_one('section.section.happenings')
    if happenings:
        builder.add_text(parent, happenings.decode_contents().strip())


def build_getting_started(builder: ContentBuilder, parent, html: str) -> None:
    soup = BeautifulSoup(html, 'lxml')
    _emit_leading_h1(builder, parent, soup)
    pane = soup.select_one('div.contentpaneopen') or soup
    intro = pane.find('p')
    if intro:
        builder.add_text(parent, intro.decode_contents().strip())
    for subsection in pane.select('div.subsection'):
        step_title = subsection.find('h2')
        title_html = step_title.decode_contents().strip() if step_title else 'Step'
        container = builder.add_container(parent, container_type='container  o-section')
        builder.add_text(container, f'<h2>{title_html}</h2>')
        for grid in subsection.select('div.hz-grid'):
            row = builder.add_row(container)
            for link in grid.select('a.no-underline'):
                col = builder.add_column(row, xs_col=12)
                builder.add_card_plain_text(col, link.decode_contents().strip())


def build_muted_card_grid_from_section(builder: ContentBuilder, parent, section_selector: str, html: str) -> None:
    soup = BeautifulSoup(html, 'lxml')
    section = soup.select_one(section_selector)
    if not section:
        return
    container = builder.add_container(parent)
    row = builder.add_row(container)
    for item in section.select('div.items-grid > div, div.split > div'):
        inner = _tile_html_from_element(item)
        if inner:
            col = builder.add_column(row, xs_col=12)
            builder.add_card_standard_text(col, inner)
