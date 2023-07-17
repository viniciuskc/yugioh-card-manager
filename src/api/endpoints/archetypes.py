from src.api.api import Api

archetypes_api = Api(
    method="get",
    resource="archetypes.php",
    description="Returns all of the current Yu-Gi-Oh! Card Archetype Names stored in the database."
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Resource:", archetypes_api.resource)
    print("Method:", archetypes_api.method)
    print("Version:", archetypes_api.version)
    print("URI:", archetypes_api.uri())
    print("Description:", archetypes_api.description)
    print("All Parameters:", str(archetypes_api.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(archetypes_api.filled_parameters()))
    print("Endpoint:", archetypes_api.url())
    print("Response:", archetypes_api.request())
