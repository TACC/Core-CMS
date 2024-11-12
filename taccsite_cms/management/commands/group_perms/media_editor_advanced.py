from django.contrib.auth.models import Group

from .util import add_perm

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Media Editor (Advanced)'
    )

    add_perm(group, 'cms', 'page', 'Can change page')
    add_perm(group, 'cms', 'page', 'Can view page')

    add_perm(group, 'cms', 'placeholder', 'Can use Structure mode')

    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can add bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can change bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can delete bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can view bootstrap4 picture')

    add_perm(group, 'djangocms_picture', 'picture', 'Can add picture')
    add_perm(group, 'djangocms_picture', 'picture', 'Can change picture')
    add_perm(group, 'djangocms_picture', 'picture', 'Can delete picture')
    add_perm(group, 'djangocms_picture', 'picture', 'Can view picture')

    add_perm(group, 'djangocms_video', 'video player', 'Can add video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can change video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can delete video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can view video player')
    add_perm(group, 'djangocms_video', 'video source', 'Can add video source')
    add_perm(group, 'djangocms_video', 'video source', 'Can change video source')
    add_perm(group, 'djangocms_video', 'video source', 'Can delete video source')
    add_perm(group, 'djangocms_video', 'video source', 'Can view video source')
    add_perm(group, 'djangocms_video', 'video track', 'Can add video track')
    add_perm(group, 'djangocms_video', 'video track', 'Can change video track')
    add_perm(group, 'djangocms_video', 'video track', 'Can delete video track')
    add_perm(group, 'djangocms_video', 'video track', 'Can view video track')

    add_perm(group, 'filer', 'Folder', 'Can add Folder')
    add_perm(group, 'filer', 'Folder', 'Can change Folder')
    add_perm(group, 'filer', 'Folder', 'Can view Folder')
    add_perm(group, 'filer', 'Folder', 'Can delete Folder')

    add_perm(group, 'filer', 'file', 'Can add file')
    add_perm(group, 'filer', 'file', 'Can change file')
    add_perm(group, 'filer', 'file', 'Can view file')
    add_perm(group, 'filer', 'file', 'Can delete file')

    add_perm(group, 'filer', 'Folder', 'Can use directory listing')
    add_perm(group, 'filer', 'Folder', 'Can view Folder')

    add_perm(group, 'filer', 'image', 'Can change image')
    add_perm(group, 'filer', 'image', 'Can view image')

    add_perm(group, 'filer', 'thumbnail option', 'Can view thumbnail option')
