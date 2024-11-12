from django.contrib.auth.models import Group

from .util import add_perm

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='News Writer (Basic)'
    )

    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can add bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can change bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can delete bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can view bootstrap4 picture')
    add_perm(group, 'cms', 'cms plugin', 'Can change cms plugin')
    add_perm(group, 'cms', 'cms plugin', 'Can view cms plugin')
    add_perm(group, 'cms', 'page', 'Can change page')
    add_perm(group, 'cms', 'page', 'Can view page')
    add_perm(group, 'cms', 'placeholder', 'Can use Structure mode')
    add_perm(group, 'djangocms_blog', 'blog article', 'Can add blog article')
    add_perm(group, 'djangocms_blog', 'blog article', 'Can change blog article')
    add_perm(group, 'djangocms_blog', 'blog article', 'Can view blog article')
    add_perm(group, 'djangocms_link', 'link', 'Can add link')
    add_perm(group, 'djangocms_link', 'link', 'Can change link')
    add_perm(group, 'djangocms_link', 'link', 'Can delete link')
    add_perm(group, 'djangocms_link', 'link', 'Can view link')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can add text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can change text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can delete text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can view text')
    add_perm(group, 'djangocms_video', 'video player', 'Can add video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can change video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can delete video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can view video player')
    add_perm(group, 'filer', 'image', 'Can add image')
    add_perm(group, 'filer', 'image', 'Can change image')
    add_perm(group, 'filer', 'image', 'Can view image')
