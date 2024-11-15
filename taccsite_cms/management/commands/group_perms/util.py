from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def add_perm(group, app_label, model_name, perm_name):
    """
    Add specific permission to a given group

    This can often be done with just the permission name e.g. —
    `group.permissions.add( Permission.objects.get( name='…' ) )`
    — but providing app and model ensure no conflict.
    """
    model = model_name.lower().replace(' ', '')
    content_type = ContentType.objects.get(
        app_label=app_label,
        model=model
    )

    group.permissions.add(
        Permission.objects.get(
            name=perm_name,
            content_type=content_type
        )
    )

def let_edit_page_content(group):
    """
    Add permissions to edit a page
    """
    add_perm(group, 'cms', 'page', 'Can view page')
    add_perm(group, 'cms', 'page', 'Can change page')

    add_perm(group, 'cms', 'placeholder', 'Can use Structure mode')

def let_view_and_change_grid(group):
    """
    Add permissions to view & edit Grid plugins
    """
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can view bootstrap4 grid container')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can change bootstrap4 grid container')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can view bootstrap4 grid column')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can change bootstrap4 grid column')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can view bootstrap4 grid row')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can change bootstrap4 grid row')

def let_add_and_delete_grid(group):
    """
    Add permissions to add & delete Grid plugins
    """
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can add bootstrap4 grid container')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid container', 'Can delete bootstrap4 grid container')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can add bootstrap4 grid column')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid column', 'Can delete bootstrap4 grid column')

    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can add bootstrap4 grid row')
    add_perm(group, 'bootstrap4_grid', 'bootstrap4 grid row', 'Can delete bootstrap4 grid row')

def let_view_and_change_text(group):
    """
    Add permissions to view & edit text-based plugins
    """
    add_perm(group, 'djangocms_link', 'link', 'Can change link')
    add_perm(group, 'djangocms_link', 'link', 'Can view link')

    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can change text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can view text')

def let_add_and_delete_text(group):
    """
    Add permissions to add & delete text-based plugins
    """
    add_perm(group, 'djangocms_link', 'link', 'Can add link')
    add_perm(group, 'djangocms_link', 'link', 'Can delete link')

    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can add text')
    add_perm(group, 'djangocms_text_ckeditor', 'text', 'Can delete text')

def let_view_and_change_media_plugins(group):
    """
    Add permissions to view & edit media plugins
    """
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can view bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can change bootstrap4 picture')

    add_perm(group, 'djangocms_picture', 'picture', 'Can view picture')
    add_perm(group, 'djangocms_picture', 'picture', 'Can change picture')

    add_perm(group, 'djangocms_video', 'video player', 'Can view video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can change video player')

    add_perm(group, 'djangocms_video', 'video source', 'Can view video source')
    add_perm(group, 'djangocms_video', 'video source', 'Can change video source')

    add_perm(group, 'djangocms_video', 'video track', 'Can view video track')
    add_perm(group, 'djangocms_video', 'video track', 'Can change video track')

def let_add_and_delete_media_plugins(group):
    """
    Add permissions to add & delete media plugins
    """
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can add bootstrap4 picture')
    add_perm(group, 'bootstrap4_picture', 'bootstrap4 picture', 'Can delete bootstrap4 picture')

    add_perm(group, 'djangocms_picture', 'picture', 'Can add picture')
    add_perm(group, 'djangocms_picture', 'picture', 'Can delete picture')

    add_perm(group, 'djangocms_video', 'video player', 'Can add video player')
    add_perm(group, 'djangocms_video', 'video player', 'Can delete video player')

    add_perm(group, 'djangocms_video', 'video source', 'Can add video source')
    add_perm(group, 'djangocms_video', 'video source', 'Can delete video source')

    add_perm(group, 'djangocms_video', 'video track', 'Can add video track')
    add_perm(group, 'djangocms_video', 'video track', 'Can delete video track')

def let_view_and_change_file(group):
    """
    Add permissions to view & change files and file plugins
    """
    # (actual files)
    add_perm(group, 'filer', 'file', 'Can change file')
    add_perm(group, 'filer', 'file', 'Can view file')
    # (file plugin instances)
    add_perm(group, 'djangocms_file', 'file', 'Can change file')
    add_perm(group, 'djangocms_file', 'file', 'Can view file')

def let_add_and_delete_file(group):
    """
    Add permissions to add & delete files
    """
    # (actual files)
    add_perm(group, 'filer', 'file', 'Can add file')
    add_perm(group, 'filer', 'file', 'Can delete file')
    # (file plugin instances)
    add_perm(group, 'djangocms_file', 'file', 'Can add file')
    add_perm(group, 'djangocms_file', 'file', 'Can delete file')

def let_view_and_change_image_file(group):
    """
    Add permissions to view & change image files
    """
    add_perm(group, 'filer', 'image', 'Can change image')
    add_perm(group, 'filer', 'image', 'Can view image')

def let_add_and_delete_image_file(group):
    """
    Add permissions to add & delete image files
    """
    add_perm(group, 'filer', 'image', 'Can add image')
    add_perm(group, 'filer', 'image', 'Can delete image')
    # HELP: An image is a file… Is this overkill?
    add_perm(group, 'filer', 'file', 'Can add file')
    add_perm(group, 'filer', 'file', 'Can delete file')

def let_view_folder(group):
    """
    Add permissions to view folders
    """

    add_perm(group, 'filer', 'Folder', 'Can use directory listing')
    add_perm(group, 'filer', 'Folder', 'Can view Folder')

    add_perm(group, 'djangocms_file', 'folder', 'Can view folder')

def let_view_and_change_folder(group):
    """
    Add permissions to view & change folders
    """

    let_view_folder(group)
    add_perm(group, 'filer', 'Folder', 'Can change Folder')

def let_add_and_delete_folder(group):
    """
    Add permissions to add & delete folders
    """

    add_perm(group, 'filer', 'Folder', 'Can add Folder')
    add_perm(group, 'filer', 'Folder', 'Can delete Folder')

def let_view_thumbnail_option(group):
    """
    Add permissions to view thumbnail options
    """

    add_perm(group, 'filer', 'thumbnail option', 'Can view thumbnail option')
