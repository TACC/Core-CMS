from django.contrib.auth.models import Group

from .util import add_perm

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Grid Editor (Advanced)'
    )

    add_perm(group, 'cms', 'page', 'Can change page')
    add_perm(group, 'cms', 'page', 'Can view page')

    add_perm(group, 'cms', 'placeholder', 'Can use Structure mode')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can add bootstrap4 grid container')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can change bootstrap4 grid container')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can delete bootstrap4 grid container')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can view bootstrap4 grid container')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can add bootstrap4 grid column')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can change bootstrap4 grid column')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can delete bootstrap4 grid column')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can view bootstrap4 grid column')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can add bootstrap4 grid row')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can change bootstrap4 grid row')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can delete bootstrap4 grid row')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can view bootstrap4 grid row')
