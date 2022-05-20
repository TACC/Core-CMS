# For proper template inheritence in custom projects, each project should be
# an app that installs Core, but we do not know how to feasibly do that yet,
# so we use this logic to emulate template inheritence in custom projects

import os

# Get template dirs given known directories
def get_template_dirs(root_dir, core_dir, custom_dir):
    if custom_dir:
        # Let custom projects load templates as if core was installed by each
        template_dirs = [
            # 1. Try to load from custom project
            os.path.join(root_dir, custom_dir, 'templates', core_dir),
            # 2. If not found, load from core
            os.path.join(root_dir, core_dir, 'templates'),
            # 3. Else, assume a (deprecated) path to a specific custom project
            os.path.join(root_dir, custom_dir),
        ]
    else:
        # Only load templates from core
        template_dirs = [
            os.path.join(root_dir, core_dir, 'templates'),
        ]

    return template_dirs
