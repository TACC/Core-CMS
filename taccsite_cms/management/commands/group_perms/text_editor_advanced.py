from django.contrib.auth.models import Group

from .util import add_perm

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Text Editor (Advanced)'
    )

    add_perm(group, 'cms', 'page', 'Can change page')
    add_perm(group, 'cms', 'page', 'Can view page')

    add_perm(group, 'cms', 'placeholder', 'Can use Structure mode')

    add_perm(group, 'djangocms_link', 'link', 'Can add link')
    add_perm(group, 'djangocms_link', 'link', 'Can change link')
    add_perm(group, 'djangocms_link', 'link', 'Can delete link')
    add_perm(group, 'djangocms_link', 'link', 'Can view link')

    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can add text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can change text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can delete text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can view text')

    add_perm(group, 'filer', 'Folder', 'Can use directory listing')
    add_perm(group, 'filer', 'Folder', 'Can add Folder')
    add_perm(group, 'filer', 'Folder', 'Can change Folder')
    add_perm(group, 'filer', 'Folder', 'Can view Folder')
    add_perm(group, 'filer', 'Folder', 'Can delete Folder')

    add_perm(group, 'filer', 'file', 'Can add file')
    add_perm(group, 'filer', 'file', 'Can change file')
    add_perm(group, 'filer', 'file', 'Can delete file')
    add_perm(group, 'filer', 'file', 'Can view file')
