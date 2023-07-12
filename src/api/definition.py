from json import loads
from math import floor
from urllib.parse import urlencode
from urllib.request import Request, urlopen

default_protocol = "https://"
default_domain = "db.ygoprodeck.com"
default_app_context = "api"
default_version = "v7"

default_headers = {'User-Agent': 'Mozilla/6.0'}

folder_full_size_images = "cards"
folder_small_size_images = "cards_small"
folder_cropped_image_art = "cards_cropped"

key_full_size_images = "image_url"
key_small_size_images = "image_url_small"
key_cropped_image_art = "image_url_cropped"


class Api:
    def __init__(self, method, resource, protocol=default_protocol, domain=default_domain,
                 app_context=default_app_context, version=default_version, headers=None, parameters=None):

        if headers is None:
            headers = default_headers

        self.__method = method
        self.__resource = resource
        self.__protocol = protocol
        self.__domain = domain
        self.__app_context = app_context
        self.__version = version
        self.__headers = headers
        self.__parameters = parameters

    def parameters(self):
        """Returns a dict with parameters that have non-null values."""

        parameters_dict = dict()

        for parameter in self.__parameters:
            if parameter.value is not None:
                parameters_dict[parameter.name] = parameter.value

        return parameters_dict

    # TODO: Implement try/except on API requests
    def request(self, parameters=None):
        """Call the API using the API uri and the provided headers and parameters, returning the response decoded in
        UTF-8."""

        if parameters is None:
            parameters = self.parameters()

        url = self.uri() + "?" + urlencode(parameters)
        request = Request(url, headers=self.__headers)
        response = urlopen(request).read().decode("utf-8")

        return response

    def uri(self):
        """Construct and return the uri using the API parameters."""

        urn = "/".join([self.__domain, self.__app_context, self.__version, self.__resource])

        return self.__protocol + urn


class Parameter:
    def __init__(self, name, data_type, description=None, mandatory=False, options=None, multi_selection=False,
                 value=None):
        self.__name = name
        self.__data_type = data_type
        self.__description = description
        self.__mandatory = mandatory
        self.__options = options
        self.__multi_selection = multi_selection
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    # TODO: In the user's input, when Enter is pressed without a typed text, set value to None (delete the value)

    # TODO: Create methods to validate the data_type and options selected of the filled parameters


# TODO: Refactor images dict inside a class
def get_images_dict(response):
    """Receives a Yu-Gi-Oh! Card information json response and returns a dictionary with the urls of all Yu-Gi-Oh!
    Card Images sorted by image size."""

    json_response = loads(response)
    if "data" not in json_response.keys():
        json_response = {"data": [json_response]}

    images_dict = {
        folder_full_size_images: {},
        folder_small_size_images: {},
        folder_cropped_image_art: {}
    }

    for card in json_response["data"]:

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


# TODO: Refactor all method below inside Parameters classes and delete them
# TODO: Implement option to clear filled fields
def fill_params(params_dict, columns=1):
    """Receives a dictionary and performs an interactive loop to fill in the values of its keys."""

    exit_fill = False

    while not exit_fill:
        print_params(params_dict, columns)
        print("Filled search parameters: " + str(get_valid_params(params_dict)) +
              "\n\nPress [Enter] to search or enter a field name to fill in.")

        param_input = input(f"> ")

        if param_input == "":
            exit_fill = True

        elif param_input in list(params_dict.keys()):
            params_dict[param_input] = input("> " + param_input + ": ")

        else:
            print(f"[ERROR] [{param_input}] option not recognized. Please enter a valid option.")

    return get_valid_params(params_dict)


def get_valid_params(params):
    """Returns a dict with keys that have non-null values."""

    params_dict = dict()

    for (key, value) in params.items():
        if value is not None:
            params_dict[key] = value

    return params_dict


def print_params(params_dict, columns=1):
    """Receives a dictionary of parameters and prints its keys tabulated in the specified number of columns."""

    print("\nThis API allows to search for a card filtering by the following fields:")

    params_keys = list(params_dict.keys())
    params_len = len(params_keys)

    params_index = 0

    while params_index < columns:
        column_index = 0
        text_to_print = ""

        while column_index < params_len:
            param = params_keys[params_index + column_index]
            indent = 2 - floor(len(param) / 8)
            text_to_print += param + ("\t" * indent)
            column_index += columns

        print(text_to_print)
        params_index += 1


if __name__ == '__main__':
    pass
