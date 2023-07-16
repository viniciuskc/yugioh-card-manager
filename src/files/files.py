from os import getcwd, makedirs, pardir, path

default_project_name = "yugioh-card-manager"


def file_exists(folder_path, file_name, file_formats, project_name=default_project_name, add_abs_path=True):
    """Checks if there is any file with the given name in any of the specified formats in the given folder."""

    file_formats_exists = []
    if add_abs_path:
        project_path = get_project_path(project_name)
    else:
        project_path = ""

    for file_format in file_formats:
        file_path = project_path + folder_path + file_name + file_format
        exists = path.exists(file_path)
        file_formats_exists.append(exists)

    return any(file_formats_exists)


def get_project_path(project_name=default_project_name):
    """Returns the absolute path of the project's root folder."""

    current_path = getcwd()
    current_folder = current_path[current_path.rfind("/"):]

    if project_name[0] != "/":
        project_folder_name = "/" + project_name
    else:
        project_folder_name = project_name

    while current_folder != project_folder_name and current_folder != "/":
        current_path = path.abspath(path.join(current_path, pardir))
        current_folder = current_path[current_path.rfind("/"):]

    if current_folder == "/":
        raise ValueError("No folder found with the project name: " + project_name)

    return current_path


def make_folder(folder_name, project_name=default_project_name):
    """Checks whether a folder exists or not. If it does not exist, create one with the specified folder name."""

    folder_name_last_char = folder_name[len(folder_name) - 1]
    project_path = get_project_path(project_name)

    if folder_name_last_char != "/":
        abs_path = project_path + "/" + folder_name + "/"
    else:
        abs_path = project_path + "/" + folder_name

    if not path.exists(abs_path):
        makedirs(abs_path)
        print("Created folder:", abs_path)

    return abs_path


if __name__ == '__main__':
    path = get_project_path(default_project_name)
    print("Project path: " + path)
