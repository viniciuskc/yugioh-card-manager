from json import loads
from shutil import copyfileobj
from src.files import files
from time import sleep
import requests

images_default_folder_name = "images/"


# TODO: Check whether the provided response contains the key "card_images", if not, throw exception
def save_images(response, folder_name=images_default_folder_name):
    """Saves all images from the api response that matches with the card id in the specified folder, naming the images
    by the card id."""

    image_key_folder = {"image_url": "cards", "image_url_small": "cards_small", "image_url_cropped": "cards_cropped"}

    for image_key in image_key_folder.keys():
        folder_path = files.make_folder(folder_name + image_key_folder[image_key] + "/")
        image_key_folder[image_key] = folder_path

    if response is not None:
        json_response = loads(response)
    else:
        print("No response images to be saved locally.")
        return None

    if "data" not in json_response.keys():
        json_response = {"data": [json_response]}

    print("Saving image files locally...")
    for card in json_response["data"]:
        card_id = str(card["id"])

        for image_key in image_key_folder.keys():
            for images in card["card_images"]:
                if str(images["id"]) == card_id:
                    image_url = images[image_key]
                    image_format = image_url[image_url.rfind("."):]
                    image_file_name = image_key_folder[image_key] + card_id + image_format

                    image_formats = [".jpeg", ".jpg", ".png", ".webp"]

                    if files.file_exists(image_key_folder[image_key], card_id, image_formats, add_abs_path=False):
                        return_text = "Image already saved locally: " + image_file_name
                        print(return_text)

                    else:
                        image_data = requests.get(image_url, stream=True)
                        with open(image_file_name, 'wb') as img:
                            copyfileobj(image_data.raw, img)

                        return_text = "Image saved locally as: " + image_file_name
                        print(return_text)
                        sleep(0.1)
