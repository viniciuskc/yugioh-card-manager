from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from time import sleep

# Yu-Gi-Oh! API Official Doc: https://ygoprodeck.com/api-guide/

default_protocol = "https://"
default_domain = "db.ygoprodeck.com"
default_app_context = "api"
default_version = "v7"

default_headers = {'User-Agent': 'Mozilla/6.0'}


class Api:
    def __init__(self, method, resource, protocol=default_protocol, domain=default_domain,
                 app_context=default_app_context, version=default_version, headers=None, parameters=None):

        if headers is None:
            headers = default_headers

        self.__method = method
        self.__resource = resource
        self.__protocol = protocol
        self.__domain = domain
        self.__app_context = app_context
        self.__version = version
        self.__headers = headers
        self.__parameters = parameters

    @property
    def method(self):
        return self.__method

    @property
    def version(self):
        return self.__version

    def parameters(self):
        """Returns a list with the name of all parameters of the endpoint."""

        if self.__parameters is not None:
            parameters_list = []
            for parameter in self.__parameters:
                parameters_list += [parameter.name]
            parameters_list.sort()
        else:
            parameters_list = None

        return parameters_list

    def filled_parameters(self):
        """Returns a dict with parameters that have non-null values."""

        if self.__parameters is not None:
            parameters_dict = dict()
            for parameter in self.__parameters:
                if parameter.value is not None:
                    parameters_dict[parameter.name] = parameter.value
        else:
            parameters_dict = None

        return parameters_dict

    def reset_parameters(self):
        """Sets all parameters to None or with their default value, if a default value is configured."""

        if self.__parameters is not None:
            parameters_dict = dict()
            for parameter in self.__parameters:
                parameter.reset_value()
        else:
            parameters_dict = None

        return parameters_dict

    def request(self):
        """Call the API using the API uri and the provided headers and endpoints, returning the response decoded in
        UTF-8."""

        request = Request(self.url(), headers=self.__headers)

        try:
            response = urlopen(request).read().decode("utf-8")
        except HTTPError as error:
            response = None
            print('Status:', error.code, error.reason)
            print("Error:", error.read().decode("utf-8"))
        except URLError as error:
            response = None
            print('Reason:', error.reason)
        else:
            print('Status: 200 OK')

        sleep(0.1)

        return response

    def uri(self):
        """Construct and return the URI of the API endpoint."""

        urn = "/".join([self.__domain, self.__app_context, self.__version, self.__resource])

        return self.__protocol + urn

    def url(self):
        """Construct and return the URL of the API request."""

        if self.__parameters is None:
            url = self.uri()
        else:
            parameters = self.filled_parameters()
            url = self.uri() + "?" + urlencode(parameters)

        return url


class Parameter:
    def __init__(self, name, data_type, description=None, mandatory=False, options=None, multi_selection=False,
                 default_value=None):
        self.__name = name
        self.__data_type = data_type
        self.__description = description
        self.__mandatory = mandatory
        self.__options = options
        self.__multi_selection = multi_selection
        self.__default_value = default_value
        self.__value = default_value

    @property
    def name(self):
        return self.__name

    @property
    def data_type(self):
        return self.__data_type

    @property
    def description(self):
        return self.__description

    @property
    def mandatory(self):
        return self.__mandatory

    @property
    def options(self):
        return self.__options

    @property
    def multi_selection(self):
        return self.__multi_selection

    @property
    def default_value(self):
        return self.__default_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def reset_value(self):
        if self.__default_value is not None:
            self.value = self.__default_value
        else:
            self.value = None
    # TODO: In the user's input, when Enter is pressed without a typed text, set value to None (delete the value)

    # TODO: Create methods to validate the data_type and options selected of the filled endpoints


if __name__ == '__main__':
    pass
