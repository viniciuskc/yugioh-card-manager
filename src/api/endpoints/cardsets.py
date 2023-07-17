from src.api.api import Api

card_sets_api = Api(
    method="get",
    resource="cardsets.php",
    description="Returns all of the current Yu-Gi-Oh! Card Set Names stored in the database."
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Resource:", card_sets_api.resource)
    print("Method:", card_sets_api.method)
    print("Version:", card_sets_api.version)
    print("URI:", card_sets_api.uri())
    print("Description:", card_sets_api.description)
    print("All Parameters:", str(card_sets_api.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(card_sets_api.filled_parameters()))
    print("Endpoint:", card_sets_api.url())
    # print("Response:", card_sets.request())
