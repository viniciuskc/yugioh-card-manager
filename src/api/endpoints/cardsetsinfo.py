from src.api.api import Api
from src.api.parameters.cardsetsinfo import *

card_sets_info = Api(
    method="get",
    resource="cardsetsinfo.php",
    parameters=[set_code]
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", card_sets_info.method)
    print("Version:", card_sets_info.version)
    print("URI:", card_sets_info.uri())
    print("All Parameters:", str(card_sets_info.parameters()))
    print("------------------------------------------------------------")
    set_code.value = "LDK2-ENY01"
    print("Parameters:", str(card_sets_info.filled_parameters()))
    print("Endpoint:", card_sets_info.url())
    print("Response:", card_sets_info.request())
