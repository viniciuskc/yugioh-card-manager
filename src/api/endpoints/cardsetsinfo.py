from src.api.api import Api
from src.api.parameters import cardsetsinfo

api = Api(
    method="get",
    resource="cardsetsinfo.php",
    parameters=[cardsetsinfo.set_code]
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", api.method)
    print("Version:", api.version)
    print("URI:", api.uri())
    print("All Parameters:", str(api.parameters()))
    print("------------------------------------------------------------")
    cardsetsinfo.set_code.value = "LDK2-ENY01"
    print("Parameters:", str(api.filled_parameters()))
    print("Endpoint:", api.url())
    print("Response:", api.request())
