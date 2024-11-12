from django.contrib.auth.models import Group

from .util import add_perm

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='Grid Editor (Advanced)'
    )

    add_perm(group, 'cms', 'page', 'Can change page')
    add_perm(group, 'cms', 'page', 'Can view page')

    add_perm(group, 'cms', 'placeholder', 'Can use Structure mode')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can change bootstrap4 grid container')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can view bootstrap4 grid container')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can change bootstrap4 column')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can view bootstrap4 column')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid rw', 'Can change bootstrap4 rw')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid rw', 'Can view bootstrap4 rw')
