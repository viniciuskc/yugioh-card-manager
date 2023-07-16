from src.api.api import Api

card_sets = Api(method="get", resource="cardsets.php")

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", card_sets.method)
    print("Version:", card_sets.version)
    print("URI:", card_sets.uri())
    print("All Parameters:", str(card_sets.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(card_sets.filled_parameters()))
    print("Endpoint:", card_sets.url())
    # print("Response:", card_sets.request())
