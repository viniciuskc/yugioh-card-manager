from src.api.definition import Api
from src.api.parameters import get_card_info, get_card_set_info

# Yu-Gi-Oh! API Official Doc: https://ygoprodeck.com/api-guide/

get_archetypes = Api("get", "archetypes.php")
get_all_cards = Api("get", "cardsets.php")
get_card_info = Api("get", "cardinfo.php", parameters=get_card_info.params)
get_card_set_info = Api("get", "cardsetsinfo.php", parameters=get_card_set_info.params)
get_db_version = Api("get", "checkDBVer.php")
get_random_card = Api("get", "randomcard.php")


if __name__ == '__main__':
    print(get_card_info.uri())
    print(get_card_info.parameters())
    print(get_card_set_info.request())
