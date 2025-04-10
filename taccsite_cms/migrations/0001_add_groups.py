from django.db import migrations

def add_groups(apps, schema_editor):
    from taccsite_cms.management.commands.group_perms.text_editor_basic import set_group_perms as add_text_editor_basic
    from taccsite_cms.management.commands.group_perms.text_editor_advanced import set_group_perms as add_text_editor_advanced
    from taccsite_cms.management.commands.group_perms.media_editor_basic import set_group_perms as add_media_editor_basic
    from taccsite_cms.management.commands.group_perms.media_editor_advanced import set_group_perms as add_media_editor_advanced
    from taccsite_cms.management.commands.group_perms.grid_editor_basic import set_group_perms as add_grid_editor_basic
    from taccsite_cms.management.commands.group_perms.grid_editor_advanced import set_group_perms as add_grid_editor_advanced

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
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('cms', '0022_auto_20180620_1551'),
        ('djangocms_link', '0016_alter_link_cmsplugin_ptr'),
        ('djangocms_text_ckeditor', '0005_alter_text_cmsplugin_ptr'),
        ('bootstrap4_grid', '0004_remove_bootstrap4gridcolumn_column_size'),
        ('bootstrap4_picture', '0004_auto_20190703_0831'),
        ('djangocms_picture', '0011_auto_20190314_1536'),
        ('djangocms_video', '0010_videoplayer_parameters'),
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        ('djangocms_file', '0011_auto_20181211_0357'),
        ('bootstrap4_content', '0002_added_figure'),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_groups, reverse_code=remove_groups),
    ]
