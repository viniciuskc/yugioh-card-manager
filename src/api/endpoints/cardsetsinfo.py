from src.api.api import Api
from src.api.parameters.cardsetsinfo import *

card_sets_info_api = Api(
    method="get",
    resource="cardsetsinfo.php",
    description="Returns a specific Yu-Gi-Oh! Card Set information.",
    parameters=[set_code]
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Resource:", card_sets_info_api.resource)
    print("Method:", card_sets_info_api.method)
    print("Version:", card_sets_info_api.version)
    print("URI:", card_sets_info_api.uri())
    print("Description:", card_sets_info_api.description)
    print("All Parameters:", str(card_sets_info_api.parameters()))
    print("------------------------------------------------------------")
    set_code.value = "LDK2-ENY01"
    print("Parameters:", str(card_sets_info_api.filled_parameters()))
    print("Endpoint:", card_sets_info_api.url())
    print("Response:", card_sets_info_api.request())
