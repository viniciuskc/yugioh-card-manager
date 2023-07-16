from src.api.api import Api

check_db_version = Api(method="get", resource="checkDBVer.php")

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Method:", check_db_version.method)
    print("Version:", check_db_version.version)
    print("URI:", check_db_version.uri())
    print("All Parameters:", str(check_db_version.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(check_db_version.filled_parameters()))
    print("Endpoint:", check_db_version.url())
    print("Response:", check_db_version.request())
