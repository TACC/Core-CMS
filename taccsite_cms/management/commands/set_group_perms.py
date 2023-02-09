import os
import logging
import importlib

from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = f'Add permissions for new or existing group(s)'

    def add_arguments(self, parser):
        parser.add_argument('group_names', nargs='+', type=str)

    def handle(self, *args, **options):
        for group_name in options['group_names']:
            file_path = os.path.join(
                os.path.dirname(__file__),
                'group_perms',
                f'{group_name}.py'
            )
            mod_path = f'taccsite_cms.management.commands.group_perms.{group_name}'

            if os.path.isfile(file_path):
                mod = importlib.import_module(mod_path)

                mod.set_group_perms()
                logger.info(
                    f'Group permissions set for group "{group_name}"'
                )
            else:
                logger.error(
                    f'No file found to set permissions for group "{group_name}"'
                )
