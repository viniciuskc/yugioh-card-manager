from csv import DictWriter
from datetime import datetime
from json import loads
from os import makedirs, path
from requests import get
from shutil import copyfileobj
from time import time, sleep
import api
import schemas

folder_name_data = "data/"
folder_name_images = "images/"
folder_name_json = folder_name_data + "json/"


def file_doesnt_exist(folder_path, file_name, file_formats):
    """Checks if there is any file with the specified directory and name in any of the provided file formats."""

    file_formats_exists = []

    for file_format in file_formats:
        exists = path.exists(folder_path + file_name + file_format)
        file_formats_exists.append(exists)

    return not any(file_formats_exists)


def get_or_create_folder(folder_name):
    """Returns the path of the folder. If a folder with the specified name does not exist, creates a new one."""

    folder_name_last_char = folder_name[len(folder_name) - 1]

    if folder_name_last_char != "/":
        folder_name += "/"

    if not path.exists(folder_name):
        makedirs(folder_name)

    return folder_name


def save_data_in_csv(json_response, file_name, folder_name=folder_name_data):
    """Saves json response data to a csv file."""

    folder_path = get_or_create_folder(folder_name)
    file_path = folder_path + file_name + ".csv"

    response = loads(json_response)["data"]
    headers = schemas.card_info_schema

    local_time = time()
    local_datetime = datetime.fromtimestamp(local_time).strftime("%Y%m%d_%H%M%S")

    response_count = len(response)
    max_index_len = len(str(response_count))
    max_id_len = 10
    index = 0

    cards_data = []
    for card in response:
        index += 1
        index_spaces = max_index_len - len(str(index)) + 1
        id_spaces = max_id_len - len(str(card["id"]))

        print(f"\n{str(index)}{' ' * index_spaces}| id: {card['id']}{' ' * id_spaces}| name: {card['name']}")

        quantity_message = f"> Card quantity: "
        set_code_message = f"> Card set code: "

        card["quantity"] = input(quantity_message)
        if int(card["quantity"]) > 0:
            card["set_code"] = input(set_code_message)
        card["created_at"] = local_datetime

        card["frame_type"] = card["frameType"]
        del card["frameType"]

        card_data = {}
        for field in card:
            if field in headers:
                card_data[field] = card[field]

        for field in headers:
            if field not in card_data:
                card_data[field] = None

        cards_data.append(card_data)

    data = [card for card in cards_data if int(card['quantity']) > 0]

    csv_formats = [".csv"]

    print(f"\nSaving data in csv file...")
    if file_doesnt_exist(folder_path, file_name, csv_formats):
        with open(file_path, "w") as file:
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    else:
        with open(file_path, "a") as file:
            writer = DictWriter(file, fieldnames=headers)
            writer.writerows(data)

    return_text = "Data saved in: " + file_path
    print(return_text)


def save_image_files(image_url_dict, folder_name=folder_name_images):
    """Saves all images from the url dictionary in the specified folder, naming them by the card id."""

    image_folders = [api.folder_full_size_images, api.folder_small_size_images, api.folder_cropped_image_art]

    print("\nSaving image files locally...")
    for folder in image_folders:
        folder_path = get_or_create_folder(folder_name + folder + "/")

        for card in image_url_dict[folder].items():
            card_id = str(card[0])

            image_url = card[1]
            image_format = image_url[image_url.rfind("."):]
            image_file_name = folder_path + card_id + image_format

            image_formats = [".jpeg", ".jpg", ".png", ".webp"]

            if file_doesnt_exist(folder_path, card_id, image_formats):
                image_data = get(image_url, stream=True)
                with open(image_file_name, 'wb') as img:
                    copyfileobj(image_data.raw, img)

                return_text = "Image saved locally: " + image_file_name
                print(return_text)
                sleep(0.1)

            else:
                return_text = "Image already saved locally: " + image_file_name
                print(return_text)


def save_json_file(json_response, folder_name=folder_name_json):
    """Creates a new json file, saving the data from the json response in the specified folder and file names, adding
    a suffix of the operation timestamp."""

    folder_path = get_or_create_folder(folder_name)

    local_time = time()
    local_datetime = datetime.fromtimestamp(local_time).strftime("%Y%m%d_%H%M%S")

    json_file_name = folder_path + local_datetime + ".json"

    print("Saving json file locally...")
    file = open(json_file_name, "w")
    file.write(json_response)

    return_text = "Data saved locally: " + json_file_name
    print(return_text)


if __name__ == '__main__':
    pass
