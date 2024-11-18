from django.contrib.auth.models import Group

from .util import (
    add_perm,
    let_view_and_change_page_structure,
    let_view_and_change_plugin,
    let_view_and_change_text,
    let_add_and_delete_text,
    let_view_and_change_media_plugins,
    let_add_and_delete_media_plugins,
    let_view_and_change_image_file,
)

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='News Writer (Advanced)'
    )

    let_view_and_change_page_structure(group)
    let_view_and_change_plugin(group)

    let_view_and_change_text(group)
    let_add_and_delete_text(group)
    # NOTE: Consider adding these to `let…text` functions
    add_perm(group, 'bootstrap4_content', 'bootstrap4 blockquote', 'Can add bootstrap4 blockquote')
    add_perm(group, 'bootstrap4_content', 'bootstrap4 blockquote', 'Can change bootstrap4 blockquote')
    add_perm(group, 'bootstrap4_content', 'bootstrap4 blockquote', 'Can delete bootstrap4 blockquote')
    add_perm(group, 'bootstrap4_content', 'bootstrap4 blockquote', 'Can view bootstrap4 blockquote')

    let_view_and_change_media_plugins(group)
    let_add_and_delete_media_plugins(group)

    let_view_and_change_image_file(group)
    add_perm(group, 'filer', 'image', 'Can add image')

    # Add permissions to view & change & add articles
    add_perm(group, None, None, 'Can view blog article')
    add_perm(group, None, None, 'Can change blog article')
    add_perm(group, None, None, 'Can add blog article')

    # Add permissions to manage categories
    add_perm(group, None, None, 'Can add blog category')
    add_perm(group, None, None, 'Can change blog category')
    add_perm(group, None, None, 'Can delete blog category')
    add_perm(group, None, None, 'Can view blog category')

    # Add permissions to manage tags & tagged items (e.g. articles)
    add_perm(group, 'taggit', 'tag', 'Can add tag')
    add_perm(group, 'taggit', 'tag', 'Can change tag')
    add_perm(group, 'taggit', 'tag', 'Can delete tag')
    add_perm(group, 'taggit', 'tag', 'Can view tag')
    add_perm(group, 'taggit', 'tagged item', 'Can add tagged item')
    add_perm(group, 'taggit', 'tagged item', 'Can change tagged item')
    add_perm(group, 'taggit', 'tagged item', 'Can delete tagged item')
    add_perm(group, 'taggit', 'tagged item', 'Can view tagged item')
