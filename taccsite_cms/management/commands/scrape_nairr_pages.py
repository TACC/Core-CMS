"""
Fetch nairrpilot.org pages and write HTML under NAIRR_SCRAPE_ROOT.

Run inside the CMS container (local dev or Camino).

Requires beautifulsoup4 in the container (NAIRR migration only; see management/commands/README.md).
"""

from django.conf import settings

from django.core.management.base import BaseCommand, CommandError

from taccsite_cms.nairr import scrape_lib
from taccsite_cms.nairr.page_registry import scrape_targets, spec_by_slug


class Command(BaseCommand):
    help = 'Scrape nairrpilot.org pages into NAIRR_SCRAPE_ROOT (one page or --all).'

    def add_arguments(self, parser):
        parser.add_argument(
            'page',
            nargs='?',
            help='Page slug (e.g. about/overview) or scrape path; omit with --all',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Scrape every path in the NAIRR page registry',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Overwrite existing scrape files',
        )
        parser.add_argument(
            '--home',
            action='store_true',
            help='Scrape home page to home.html',
        )

    def handle(self, *args, **options):
        root = scrape_lib.scrape_root(settings)
        base = scrape_lib.base_url(settings)
        delay = getattr(settings, 'NAIRR_SCRAPE_CRAWL_DELAY', 1.0)
        root.mkdir(parents=True, exist_ok=True)

        paths = []
        if options['all']:
            paths = list(scrape_targets())
            paths.append('home')
        elif options['home']:
            paths = ['home']
        elif options['page']:
            spec = spec_by_slug(options['page'])
            if spec and spec.pattern == 'home':
                paths = ['home']
            elif spec:
                paths = [spec.scrape_path]
            else:
                paths = [options['page'].strip('/')]
        else:
            raise CommandError('Provide a page slug, --home, or --all')

        for scrape_path in paths:
            path = scrape_lib.scrape_one(
                scrape_path,
                root=root,
                base=base,
                force=options['force'],
                crawl_delay=delay,
            )
            self.stdout.write(self.style.SUCCESS(f'Wrote {path}'))

        self.stdout.write(f'Scrape root: {root}')
