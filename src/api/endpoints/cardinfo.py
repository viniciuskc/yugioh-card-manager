from src.api.api import Api
from src.api.parameters.cardinfo import *

card_info_api = Api(
    method="get",
    resource="cardinfo.php",
    description="Returns all Yu-Gi-Oh! Card information that matches the specified parameters.",
    parameters=[
        card_archetype,
        card_atk,
        card_attribute,
        card_banlist,
        card_date_region,
        card_def,
        card_end_date,
        card_fname,
        card_format,
        card_has_effect,
        card_id,
        card_language,
        card_level,
        card_link,
        card_linkmarker,
        card_misc,
        card_name,
        card_race,
        card_scale,
        card_set,
        card_sort,
        card_staple,
        card_start_date,
        card_type
    ]
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Resource:", card_info_api.resource)
    print("Method:", card_info_api.method)
    print("Version:", card_info_api.version)
    print("URI:", card_info_api.uri())
    print("Description:", card_info_api.description)
    print("All Parameters:", str(card_info_api.parameters()))
    print("------------------------------------------------------------")
    card_type.value = "Fusion Monster"
    card_attribute.value = "Fire"
    card_race.value = "Dragon"
    card_atk.value = 3500
    print("Parameters:", str(card_info_api.filled_parameters()))
    print("Endpoint:", card_info_api.url())
    print("Response:", card_info_api.request())
