"""
Global static placeholders (site_id NULL) bypass unique_together on (code, site) in
PostgreSQL, so concurrent template get_or_create can insert duplicates. Bind existing
rows to SITE_ID and drop extras.
"""

from django.conf import settings
from django.db import migrations


STATIC_PLACEHOLDER_CODES = ('header-logo', 'footer-content')


def _plugin_count(CMSPlugin, static_placeholder):
    total = 0
    for placeholder_id in (static_placeholder.draft_id, static_placeholder.public_id):
        if placeholder_id:
            total += CMSPlugin.objects.filter(placeholder_id=placeholder_id).count()
    return total


def forwards(apps, schema_editor):
    StaticPlaceholder = apps.get_model('cms', 'StaticPlaceholder')
    CMSPlugin = apps.get_model('cms', 'CMSPlugin')
    Site = apps.get_model('sites', 'Site')

    site_id = settings.SITE_ID
    if not Site.objects.filter(pk=site_id).exists():
        site_id = Site.objects.order_by('pk').values_list('pk', flat=True).first()
    if site_id is None:
        return

    for code in STATIC_PLACEHOLDER_CODES:
        global_rows = list(
            StaticPlaceholder.objects.filter(code=code, site__isnull=True).order_by('id')
        )
        if not global_rows:
            continue

        if StaticPlaceholder.objects.filter(code=code, site_id=site_id).exists():
            for row in global_rows:
                row.delete()
            continue

        global_rows.sort(key=lambda row: (-_plugin_count(CMSPlugin, row), row.pk))
        keeper = global_rows[0]
        for row in global_rows[1:]:
            row.delete()

        keeper.site_id = site_id
        keeper.save(update_fields=['site'])


class Migration(migrations.Migration):

    dependencies = [
        ('taccsite_cms', '0002_remove_old_system_monitor_table'),
        ('cms', '0022_auto_20180620_1551'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
