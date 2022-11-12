input_params_get_card_info = {
    "archetype": None,
    "atk": 3500,
    "attribute": "FIRE",
    "banlist": None,
    "cardset": None,
    "dateregion": None,
    "def": 2000,
    "enddate": None,
    "fname": None,
    "format": None,
    "has_effect": None,
    "id": None,
    "language": None,
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

input_params_get_card_set_info = {
    "setcode": None
}


def get_valid_params(params):
    params_dict = dict()

    for (key, value) in params.items():
        if value is not None:
            params_dict[key] = value

    return params_dict


if __name__ == '__main__':
    pass
