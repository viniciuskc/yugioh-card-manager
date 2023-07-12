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
