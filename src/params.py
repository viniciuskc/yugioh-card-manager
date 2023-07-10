from math import floor

params_get_card_info = {
    "archetype": None,
    "atk": None,
    "attribute": None,
    "banlist": None,
    "cardset": None,
    "dateregion": None,
    "def": None,
    "enddate": None,
    "fname": None,
    "format": None,
    "has_effect": None,
    "id": None,
    "language": "pt",
    "level": None,
    "link": None,
    "linkmarker": None,
    "misc": None,
    "name": None,
    "race": None,
    "scale": None,
    "sort": None,
    "staple": None,
    "startdate": None,
    "type": None
}

params_get_card_set_info = {
    "setcode": None
}


# TODO: [1] Implement option to clear filled fields
# TODO: [2] Implement input validator (string, int etc)
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
