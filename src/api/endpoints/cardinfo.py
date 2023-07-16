from src.api.api import Api
from src.api.parameters import cardinfo

api = Api(
    method="get",
    resource="cardinfo.php",
    parameters=[
        cardinfo.card_archetype,
        cardinfo.card_atk,
        cardinfo.card_attribute,
        cardinfo.card_banlist,
        cardinfo.card_date_region,
        cardinfo.card_def,
        cardinfo.card_end_date,
        cardinfo.card_fname,
        cardinfo.card_format,
        cardinfo.card_has_effect,
        cardinfo.card_id,
        cardinfo.card_language,
        cardinfo.card_level,
        cardinfo.card_link,
        cardinfo.card_linkmarker,
        cardinfo.card_misc,
        cardinfo.card_name,
        cardinfo.card_race,
        cardinfo.card_scale,
        cardinfo.card_set,
        cardinfo.card_sort,
        cardinfo.card_staple,
        cardinfo.card_start_date,
        cardinfo.card_type
    ]
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", api.method)
    print("Version:", api.version)
    print("URI:", api.uri())
    print("All Parameters:", str(api.parameters()))
    print("------------------------------------------------------------")
    cardinfo.card_type.value = "Fusion Monster"
    cardinfo.card_attribute.value = "Fire"
    cardinfo.card_race.value = "Dragon"
    cardinfo.card_atk.value = 3500
    print("Parameters:", str(api.filled_parameters()))
    print("Endpoint:", api.url())
    print("Response:", api.request())
