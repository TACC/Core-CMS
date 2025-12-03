import logging
from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .djangocms_bootstrap4.contrib.bootstrap4_link.extend import extendBootstrap4LinkPlugin
from .djangocms_blog.patch import patchDjangoCMSBlog

logger = logging.getLogger(f"portal.{__name__}")

class TaccsiteCmsConfig(AppConfig):
    name = 'taccsite_cms'
    verbose_name = 'TACC CMS'

    def ready(self):
        post_migrate.connect(self.create_groups, sender=self)
        extendBootstrap4LinkPlugin()
        patchDjangoCMSBlog()

    def create_groups(self, sender, **kwargs):
        from django.contrib.auth.models import Group

        from .management.commands.group_perms.text_editor_basic import \
            set_group_perms as add_text_editor_basic, GROUP_NAME
        from .management.commands.group_perms.text_editor_advanced import \
            set_group_perms as add_text_editor_advanced
        from .management.commands.group_perms.media_editor_basic import \
            set_group_perms as add_media_editor_basic
        from .management.commands.group_perms.media_editor_advanced import \
            set_group_perms as add_media_editor_advanced
        from .management.commands.group_perms.grid_editor_basic import \
            set_group_perms as add_grid_editor_basic
        from .management.commands.group_perms.grid_editor_advanced import \
            set_group_perms as add_grid_editor_advanced

        groups_exist = Group.objects.filter(name=GROUP_NAME).exists()
        action = 'Updating' if groups_exist else 'Creating'

        logger.info(f'{action} CMS groups via post_migrate signal')
        try:
            add_text_editor_basic()
            add_text_editor_advanced()
            add_media_editor_basic()
            add_media_editor_advanced()
            add_grid_editor_basic()
            add_grid_editor_advanced()
            logger.info(f'Finished {action.lower()} CMS groups')
        except Exception as e:
            logger.error(f'Error creating CMS groups: {e}', exc_info=True)
