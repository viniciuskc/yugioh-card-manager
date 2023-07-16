from collections import abc
from csv import DictWriter
from datetime import datetime
from json import loads
from src.writer import files
from time import time

csv_default_folder_name = "data/csv/"
json_default_folder_name = "data/json/"


class Column:
    def __init__(self, name, response_name, data_type, primary_key=False, nullable=True, array=False, options=None,
                 description=None):

        if primary_key:
            nullable = False

        self.__name = name
        self.__response_name = response_name
        self.__data_type = data_type
        self.__primary_key = primary_key
        self.__nullable = nullable
        self.__array = array
        self.__options = options
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def response_name(self):
        return self.__response_name

    @property
    def data_type(self):
        return self.__data_type

    @property
    def nullable(self):
        return self.__nullable

    @property
    def array(self):
        return self.__array

    @property
    def primary_key(self):
        return self.__primary_key

    @property
    def options(self):
        return self.__options

    @property
    def description(self):
        return self.__description


class Dataset:
    def __init__(self, name, columns, sort=None, write_mode="append", description=None):
        self.__name = name
        self.__columns = columns
        self.__sort = sort
        self.__write_mode = write_mode
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def sort(self):
        return self.__sort

    @property
    def write_mode(self):
        return self.__write_mode

    @property
    def description(self):
        return self.__description

    def columns(self):
        """Returns a list with all dataset columns sorted by name."""
        column_list = []
        for column in self.__columns:
            column_list += [column.name]
        column_list.sort()
        return column_list

    def columns_alias(self):
        """Returns a dict with all dataset columns and their equivalent key in the api response."""
        column_dict = dict()
        for column in self.__columns:
            column_dict[column.name] = column.response_name
        return column_dict

    def primary_keys(self):
        """Returns a list with all primary key columns of the dataset sorted by name."""
        pk_list = []
        for column in self.__columns:
            if column.primary_key:
                pk_list += [column.name]
        pk_list.sort()
        return pk_list

    def parse_response(self, response):
        """Parses the provided response to the dataset schema."""

        columns_alias = self.columns_alias()

        json_response = loads(response)
        if "data" not in json_response.keys():
            json_response = {"data": [json_response]}

        local_time = time()
        local_datetime = datetime.fromtimestamp(local_time).strftime("%Y%m%d_%H%M%S")

        data = []
        for item in json_response["data"]:
            row = dict()

            item["datetime"] = local_datetime

            for column_name in columns_alias.keys():

                alias_is_array = isinstance(columns_alias[column_name], abc.Sequence)
                alias_is_not_string = isinstance(columns_alias[column_name], str)

                if alias_is_array and not alias_is_not_string:
                    response_value = None
                    for alias in columns_alias[column_name]:
                        if item.get(alias) is not None:
                            response_value = item[alias]
                        else:
                            response_value = None
                    row[column_name] = response_value

                else:
                    if item.get(columns_alias[column_name]) is not None:
                        response_value = item[columns_alias[column_name]]
                        row[column_name] = response_value
                    else:
                        row[column_name] = None

            data.append(row)

        return data

    def save_csv(self, response, folder_name=csv_default_folder_name):
        """Saves the data from the provided response in a csv file."""

        data = self.parse_response(response)

        folder_path = files.make_folder(folder_name)
        file_path = folder_path + self.__name + ".csv"

        headers = self.columns()

        csv_formats = [".csv"]

        print(f"Saving data in csv file locally...")
        if files.file_exists(folder_path, self.__name, csv_formats):
            with open(file_path, "a") as file:
                writer = DictWriter(file, fieldnames=headers)
                writer.writerows(data)
                mode_text = "Data appended in csv: "
        else:
            with open(file_path, "w") as file:
                writer = DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
                mode_text = "Csv saved locally as: "

        return_text = mode_text + file_path
        print(return_text)

    def save_json(self, response, folder_name=json_default_folder_name):
        """Saves the data from the provided response in a json file."""

        data = self.parse_response(response)

        folder_path = files.make_folder(folder_name)

        local_time = time()
        local_datetime = datetime.fromtimestamp(local_time).strftime("%Y%m%d_%H%M%S")

        json_file_name = folder_path + self.__name + local_datetime + ".json"

        print("Saving json file locally...")
        file = open(json_file_name, "w")
        file.write(str(data))

        return_text = "Json saved locally as: " + json_file_name
        print(return_text)


if __name__ == '__main__':
    pass
