from src.api.definition import Api

api = Api(method="get", resource="cardsets.php")

if __name__ == '__main__':
    print("Method: " + api.method)
    print("Version: " + api.version)
    print("URI: " + api.uri())
    print("Parameters: " + str(api.parameters()))
