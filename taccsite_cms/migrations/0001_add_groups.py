from django.db import migrations

# No-op since group creation became handled by post_migrate signal (see apps.py)

# Retained for backwards-compatibility / migration history integrity

def noop(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(noop),
    ]
