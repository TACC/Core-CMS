from cms.models import Page
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Lists all CMS pages and their templates with full URLs'

    def handle(self, *args, **options):
        pages = Page.objects.filter(publisher_is_draft=False).order_by('node__path')
        current_site = Site.objects.get_current()
        domain = current_site.domain
        protocol = 'https' if domain and domain != 'localhost' else 'http'

        template_usage = {}

        for page in pages:
            template = page.template
            if template not in template_usage:
                template_usage[template] = []
            url = page.get_absolute_url()
            full_url = f"{protocol}://{domain}{url}"
            template_usage[template].append((page.get_title(), full_url))

        for template, pages in template_usage.items():
            templateOutput = f'"{template}"' if template != 'INHERIT' else template
            self.stdout.write(f'\nTEMPLATE: {templateOutput}')
            self.stdout.write('PAGES:')
            for title, url in pages:
                self.stdout.write(f'- {title} ({url})')
