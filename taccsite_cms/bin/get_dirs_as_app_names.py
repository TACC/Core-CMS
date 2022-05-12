import os

# Convert directories under given path to a list of app names
def get_dirs_as_app_names(path):
    sep = os.path.sep
    names = []

    for entry in os.scandir(path):
        is_app = entry.path.find('_readme') == -1

        if entry.is_dir() and is_app:
            name = entry.path

            # Remove root directory in containers
            name = name.replace(sep + 'code' + sep, '')
            # Remove root directory in non-container deploys
            name = name.replace(sep + 'srv' + sep + 'taccsite' + sep, '')
            # Convert path to app name
            name = name.replace(sep, '.')

            names.append(name)

    return names
