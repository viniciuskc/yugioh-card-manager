import json
import urllib.parse
import urllib.request

default_headers = {'User-Agent': 'Mozilla/6.0'}

default_params_get_card_info = {}
default_params_get_card_set_info = {"setcode": ""}

url_get_all_archetypes = "https://db.ygoprodeck.com/api/v7/archetypes.php"
url_get_all_card_sets = "https://db.ygoprodeck.com/api/v7/cardsets.php"
url_get_card_info = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
url_get_card_set_info = "https://db.ygoprodeck.com/api/v7/cardsetsinfo.php"
url_get_database_version = "https://db.ygoprodeck.com/api/v7/checkDBVer.php"
url_get_random_card = "https://db.ygoprodeck.com/api/v7/randomcard.php"


def api_request(url, headers, params=None):
    if params is None:
        params = {}

    query_string = urllib.parse.urlencode(params)
    full_url = url + "?" + query_string
    request = urllib.request.Request(full_url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    return data


def get_all_archetypes(headers=None):
    if headers is None:
        headers = default_headers

    return api_request(url_get_all_card_sets, headers)


def get_all_card_sets(headers=None):
    if headers is None:
        headers = default_headers

    return api_request(url_get_all_card_sets, headers)


def get_card_info(headers=None, params=None):
    if headers is None:
        headers = default_headers

    if params is None:
        params = default_params_get_card_info

    return api_request(url_get_card_info, headers, params)


def get_card_set_info(headers=None, params=None):
    if headers is None:
        headers = default_headers

    if params is None:
        params = default_params_get_card_set_info

    return api_request(url_get_card_set_info, headers, params)


def get_database_version(headers=None):
    if headers is None:
        headers = default_headers

    return api_request(url_get_database_version, headers)


def get_random_card(headers=None):
    if headers is None:
        headers = default_headers

    return api_request(url_get_random_card, headers)


if __name__ == '__main__':
    pass
