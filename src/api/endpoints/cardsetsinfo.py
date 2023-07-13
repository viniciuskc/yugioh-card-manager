from src.api.definition import Api, Parameter

api = Api(
    method="get",
    resource="cardsetsinfo.php",
    parameters=[
        Parameter(name="setcode",
                  data_type="string",
                  mandatory=True,
                  description="Filter the cards by set code [e.g. 'SDY-046'].",
                  value="LDK2-ENJ41")
    ]
)

if __name__ == '__main__':
    print("Method: " + api.method)
    print("Version: " + api.version)
    print("URI: " + api.uri())
    print("Parameters: " + str(api.parameters()))
