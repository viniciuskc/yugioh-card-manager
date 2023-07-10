from json import loads
import urllib.parse
import urllib.request

default_headers = {'User-Agent': 'Mozilla/6.0'}

default_params_get_card_info = {}
default_params_get_card_set_info = {"setcode": ""}

# Yu-Gi-Oh! API Official Doc: https://ygoprodeck.com/api-guide/

url_api = "https://db.ygoprodeck.com/api/v7/"

url_get_all_archetypes = url_api + "archetypes.php"
url_get_all_card_sets = url_api + "cardsets.php"
url_get_card_info = url_api + "cardinfo.php"
url_get_card_set_info = url_api + "cardsetsinfo.php"
url_get_database_version = url_api + "checkDBVer.php"
url_get_random_card = url_api + "randomcard.php"

url_images = "https://images.ygoprodeck.com/images/"

folder_full_size_images = "cards"
folder_small_size_images = "cards_small"
folder_cropped_image_art = "cards_cropped"

key_full_size_images = "image_url"
key_small_size_images = "image_url_small"
key_cropped_image_art = "image_url_cropped"


# TODO: Implement try/except on API calls
def api_request(url, headers, params=None):
    """Call the API using the url, headers and params provided and returns its response decoded in UTF-8."""

    if params is None:
        params = {}

    query_string = urllib.parse.urlencode(params)
    full_url = url + "?" + query_string
    request = urllib.request.Request(full_url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

    return data


def get_all_archetypes(headers=None):
    """Returns all the current Yu-Gi-Oh! Card Archetype Names stored in the database."""

    if headers is None:
        headers = default_headers

    return api_request(url_get_all_archetypes, headers)


def get_all_card_sets(headers=None):
    """Returns all the current Yu-Gi-Oh! Card Set Names stored in the database."""

    if headers is None:
        headers = default_headers

    return api_request(url_get_all_card_sets, headers)


def get_card_info(headers=None, params=None):
    """Returns a Yu-Gi-Oh! Card Set information.

    Requires a parameter `setcode`."""

    if headers is None:
        headers = default_headers

    if params is None:
        params = default_params_get_card_info

    return api_request(url_get_card_info, headers, params)


def get_card_set_info(headers=None, params=None):
    """Returns a Yu-Gi-Oh! Card information.

    It's possible to pass multiple parameters to filter the information retrieved."""

    if headers is None:
        headers = default_headers

    if params is None:
        params = default_params_get_card_set_info

    return api_request(url_get_card_set_info, headers, params)


def get_database_version(headers=None):
    """Returns the current version of the database."""

    if headers is None:
        headers = default_headers

    return api_request(url_get_database_version, headers)


def get_random_card(headers=None):
    """Returns a random Yu-Gi-Oh! Card information from the database."""

    if headers is None:
        headers = default_headers

    return api_request(url_get_random_card, headers)


def images_url_dict(json_response):
    """Receives a Yu-Gi-Oh! Card information json response and returns a dictionary with the urls of all Yu-Gi-Oh!
    Card Images sorted by image size."""

    json_data = loads(json_response)
    if "data" not in json_data.keys():
        json_data = {"data": [json_data]}

    images_dict = {
        folder_full_size_images: {},
        folder_small_size_images: {},
        folder_cropped_image_art: {}
    }

    for card in json_data["data"]:

        if len(str(card["id"])) < 8:
            card_id = "0" + str(card["id"])
        else:
            card_id = str(card["id"])

        for image in card["card_images"]:

            if key_full_size_images in image.keys():
                image_url = image[key_full_size_images]
                images_dict[folder_full_size_images][card_id] = image_url

            if key_small_size_images in image.keys():
                image_url_small = image[key_small_size_images]
                images_dict[folder_small_size_images][card_id] = image_url_small

            if key_cropped_image_art in image.keys():
                image_url_cropped = image[key_cropped_image_art]
                images_dict[folder_cropped_image_art][card_id] = image_url_cropped

    return images_dict


if __name__ == '__main__':
    pass
