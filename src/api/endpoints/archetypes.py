from src.api.api import Api

archetypes = Api(method="get", resource="archetypes.php")

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", archetypes.method)
    print("Version:", archetypes.version)
    print("URI:", archetypes.uri())
    print("All Parameters:", str(archetypes.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(archetypes.filled_parameters()))
    print("Endpoint:", archetypes.url())
    print("Response:", archetypes.request())
