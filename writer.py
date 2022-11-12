import time
import datetime
import os

folder_name = "data"


def get_or_create_folder():
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def write_json_file(file_name_prefix, data):
    get_or_create_folder()

    local_time = time.time()
    local_datetime = datetime.datetime.fromtimestamp(local_time).strftime('%Y%m%d_%H%M%S')

    folder_path = folder_name + "/"
    json_file = folder_path + file_name_prefix + local_datetime + ".json"

    file = open(json_file, "w")
    file.write(data)
    return_text = "Data saved in the file: " + json_file
    print(return_text)


if __name__ == '__main__':
    pass
