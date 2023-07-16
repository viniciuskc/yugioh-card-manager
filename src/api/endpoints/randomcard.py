from src.api.api import Api

random_card = Api(method="get", resource="randomcard.php")

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", random_card.method)
    print("Version:", random_card.version)
    print("URI:", random_card.uri())
    print("All Parameters:", str(random_card.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(random_card.filled_parameters()))
    print("Endpoint:", random_card.url())
    print("Response:", random_card.request())
