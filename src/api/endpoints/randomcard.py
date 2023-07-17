from src.api.api import Api

random_card_api = Api(
    method="get",
    resource="randomcard.php",
    description="Returns a random Yu-Gi-Oh! Card information from the database."
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Resource:", random_card_api.resource)
    print("Method:", random_card_api.method)
    print("Version:", random_card_api.version)
    print("URI:", random_card_api.uri())
    print("Description:", random_card_api.description)
    print("All Parameters:", str(random_card_api.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(random_card_api.filled_parameters()))
    print("Endpoint:", random_card_api.url())
    print("Response:", random_card_api.request())
