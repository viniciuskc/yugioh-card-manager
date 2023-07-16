from json import dumps, loads

# TODO: File not working, finish refactoring the api definitions and then refactor methods in this file


def search_card_details(response):
    """Displays card id selection and prints the selected card details based on provided response json."""

    response_json = loads(response)["data"]

    card_id_message = "\n> Enter a card id from the result list: "
    card_id_input = str(input(card_id_message)).lower()

    output_json = [card for card in response_json if str(card["id"]) == card_id_input]
    print(f"\nCard {card_id_input} details:\n" + dumps(output_json[0], indent=2))


def search_card():
    """Executes the Yu-Gi-Oh! Card search flow and returns a json response."""

    empty_parameters = parameters.params_get_card_info
    valid_parameters = parameters.fill_params(empty_parameters, 6)

    response = api.get_card_info.request(params=valid_parameters)
    response_count = len(loads(response)["data"])
    print(f"\nSearch returned {response_count} results:")

    index = 0
    max_index_len = len(str(response_count))
    max_id_len = 10

    for card in loads(response)["data"]:
        index += 1
        index_spaces = max_index_len - len(str(index)) + 1
        id_spaces = max_id_len - len(str(card["id"]))

        print(f"{str(index)}{' ' * index_spaces}| id: {card['id']}{' ' * id_spaces}| name: {card['name']}")

    return response


def search_card_set():
    """Executes the Yu-Gi-Oh! Card Set search flow."""

    empty_parameters = parameters.params_get_card_set_info
    valid_parameters = parameters.fill_params(empty_parameters, 1)

    response = api.get_card_set_info.request(params=valid_parameters)

    print("\nResponse:\n" + dumps(loads(response), indent=2))


def search_random_card():
    """Executes the Yu-Gi-Oh! Card random search flow and saves the images from the result in the local images
    folder."""

    response = api.get_random_card.request()
    print("\nResponse:\n" + dumps(loads(response), indent=2))

    return response

# TODO: Refactor all method below inside Parameters classes and delete them
# TODO: Implement option to clear filled fields
#
# def fill_params(params_dict, columns=1):
#     """Receives a dictionary and performs an interactive loop to fill in the values of its keys."""
#
#     exit_fill = False
#
#     while not exit_fill:
#         print_params(params_dict, columns)
#         print("Filled search endpoints: " + str(get_valid_params(params_dict)) +
#               "\n\nPress [Enter] to search or enter a field name to fill in.")
#
#         param_input = input(f"> ")
#
#         if param_input == "":
#             exit_fill = True
#
#         elif param_input in list(params_dict.keys()):
#             params_dict[param_input] = input("> " + param_input + ": ")
#
#         else:
#             print(f"[ERROR] [{param_input}] option not recognized. Please enter a valid option.")
#
#     return get_valid_params(params_dict)
#
#
# def print_params(params_dict, columns=1):
#     """Receives a dictionary of endpoints and prints its keys tabulated in the specified number of columns."""
#
#     print("\nThis API allows to search for a card filtering by the following fields:")
#
#     params_keys = list(params_dict.keys())
#     params_len = len(params_keys)
#
#     params_index = 0
#
#     while params_index < columns:
#         column_index = 0
#         text_to_print = ""
#
#         while column_index < params_len:
#             param = params_keys[params_index + column_index]
#             indent = 2 - floor(len(param) / 8)
#             text_to_print += param + ("\t" * indent)
#             column_index += columns
#
#         print(text_to_print)
#         params_index += 1
