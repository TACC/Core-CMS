from django.db import migrations

def add_groups(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.text_editor_basic import set_group_perms as add_text_editor_basic
    from taccsite_cms.management.commands.group_perms.text_editor_advanced import set_group_perms as add_text_editor_advanced
    from taccsite_cms.management.commands.group_perms.media_editor_basic import set_group_perms as add_media_editor_basic
    from taccsite_cms.management.commands.group_perms.media_editor_advanced import set_group_perms as add_media_editor_advanced
    from taccsite_cms.management.commands.group_perms.grid_editor_basic import set_group_perms as add_grid_editor_basic
    from taccsite_cms.management.commands.group_perms.grid_editor_advanced import set_group_perms as add_grid_editor_advanced

    # Ensure permissions are created
    from django.contrib.auth.management import create_permissions
    from django.apps import apps as django_apps
    for app_config in django_apps.get_app_configs():
        create_permissions(app_config, verbosity=0)

    add_text_editor_basic()
    add_text_editor_advanced()
    add_media_editor_basic()
    add_media_editor_advanced()
    add_grid_editor_basic()
    add_grid_editor_advanced()

def remove_groups(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.text_editor_basic import GROUP_NAME as text_editor_basic_name
    from taccsite_cms.management.commands.group_perms.text_editor_advanced import GROUP_NAME as text_editor_advanced_name
    from taccsite_cms.management.commands.group_perms.media_editor_basic import GROUP_NAME as media_editor_basic_name
    from taccsite_cms.management.commands.group_perms.media_editor_advanced import GROUP_NAME as media_editor_advanced_name
    from taccsite_cms.management.commands.group_perms.grid_editor_basic import GROUP_NAME as grid_editor_basic_name
    from taccsite_cms.management.commands.group_perms.grid_editor_advanced import GROUP_NAME as grid_editor_advanced_name

    Group = apps.get_model('auth', 'Group')

    group_names = [
        text_editor_basic_name,
        text_editor_advanced_name,
        media_editor_basic_name,
        media_editor_advanced_name,
        grid_editor_basic_name,
        grid_editor_advanced_name,
    ]

    Group.objects.filter(name__in=group_names).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial'),
        ('contenttypes', '0001_initial'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_groups, reverse_code=remove_groups),
    ]
