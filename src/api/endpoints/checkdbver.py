from src.api.api import Api

check_db_version_api = Api(
    method="get",
    resource="checkDBVer.php",
    description="Returns the current version of the database."
)

if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Resource:", check_db_version_api.resource)
    print("Method:", check_db_version_api.method)
    print("Version:", check_db_version_api.version)
    print("URI:", check_db_version_api.uri())
    print("Description:", check_db_version_api.description)
    print("All Parameters:", str(check_db_version_api.parameters()))
    print("------------------------------------------------------------")
    print("Parameters:", str(check_db_version_api.filled_parameters()))
    print("Endpoint:", check_db_version_api.url())
    print("Response:", check_db_version_api.request())
