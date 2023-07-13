from src.api.definition import Api

api = Api(method="get", resource="checkDBVer.php")

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method: " + api.method)
    print("Version: " + api.version)
    print("URI: " + api.uri())
    print("All Parameters: " + str(api.parameters()))
    print("------------------------------------------------------------")
    print("Parameters: " + str(api.filled_parameters()))
    print("Endpoint: " + api.url())
    print("Response:" + api.request())
