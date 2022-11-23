import time
import datetime
import json
import os
import requests
import shutil

folder_name_data = "data"
folder_name_image = "image"


def get_or_create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def save_images(file_name_prefix, data):
    get_or_create_folder(folder_name_image)
    folder_path = folder_name_image + "/"

    json_data = json.loads(data)

    for card in json_data["data"]:
        card_id = str(card["id"])
        for image in card["card_images"]:
            image_id = str(image["id"])

            local_time = time.time()
            local_datetime = datetime.datetime.fromtimestamp(local_time).strftime('%Y%m%d_%H%M%S')

            image_url = image["image_url"]
            image_format = image_url[image_url.rfind("."):]
            image_data = requests.get(image_url, stream=True)
            image_file = folder_path + file_name_prefix + card_id + "_" + image_id + "_" + local_datetime + image_format

            with open(image_file, 'wb') as img:
                shutil.copyfileobj(image_data.raw, img)
            return_text = "Card image saved as: " + image_file
            print(return_text)

            image_url_small = image[f"image_url_small"]
            image_format_small = image_url_small[image_url_small.rfind("."):]
            image_data_small = requests.get(image_url_small, stream=True)
            image_file_small = folder_path + file_name_prefix + card_id + "_" + image_id + "_small_" + \
                local_datetime + image_format_small

            with open(image_file_small, 'wb') as img:
                shutil.copyfileobj(image_data_small.raw, img)
            return_text_small = "Card image small saved as: " + image_file_small
            print(return_text_small)


def write_json_file(file_name_prefix, data):
    get_or_create_folder(folder_name_data)
    folder_path = folder_name_data + "/"

    local_time = time.time()
    local_datetime = datetime.datetime.fromtimestamp(local_time).strftime('%Y%m%d_%H%M%S')

    json_file = folder_path + file_name_prefix + local_datetime + ".json"

    file = open(json_file, "w")
    file.write(data)
    return_text = "Data saved as: " + json_file
    print(return_text)


if __name__ == '__main__':
    pass
