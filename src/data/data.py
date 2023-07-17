from collections import abc
from datetime import datetime
from json import loads
from os.path import exists

from pandas import DataFrame
from src.files import files
from time import time

csv_default_folder_name = "data/csv/"
json_default_folder_name = "data/json/"


class Column:
    def __init__(self, name, response_key, data_type, primary_key=False, nullable=True, array=False, options=None,
                 description=None):

        if primary_key:
            nullable = False

        self.__name = name
        self.__response_key = response_key
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
    def response_key(self):
        return self.__response_key

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
    def __init__(self, name, columns, nested_key=None, sort=None, write_mode="append", description=None):
        self.__name = name
        self.__columns = columns
        self.__nested_key = nested_key
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
            column_dict[column.name] = column.response_key
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

        if response is not None:
            json_response = loads(response)
        else:
            return None

        if "data" not in json_response.keys():
            json_response = {"data": [json_response]}

        local_time = time()
        local_datetime = datetime.fromtimestamp(local_time).strftime("%Y%m%d_%H%M%S")

        data = []

        for item in json_response["data"]:
            item["datetime"] = local_datetime

            # Data handling for datasets with more than one row of data inside nested fields
            if self.__nested_key is not None:
                row_index = 0
                len_nested_field = len(item[self.__nested_key])
            else:
                row_index = 0
                len_nested_field = 1

            while row_index < len_nested_field:
                row = dict()
                for column_name in columns_alias.keys():

                    alias_is_not_string = not isinstance(columns_alias[column_name], str)
                    alias_is_array = isinstance(columns_alias[column_name], abc.Sequence)

                    # Data handling for nested fields of the response
                    if alias_is_not_string and alias_is_array:
                        len_alias = len(columns_alias[column_name])
                        item_iterator = item
                        response_value = None

                        for alias in columns_alias[column_name]:
                            if item_iterator is not None and item_iterator.get(alias) is not None:

                                item_is_array = isinstance(item_iterator[alias], abc.Sequence)
                                item_is_not_string = not isinstance(item_iterator[alias], str)

                                # Data handling to get only the first item of a nested field
                                if item_is_array and item_is_not_string and len_alias > 1:
                                    item_iterator = item_iterator[alias][row_index]

                                else:
                                    item_iterator = item_iterator[alias]

                            else:
                                item_iterator = None

                            response_value = item_iterator
                            len_alias -= 1

                        row[column_name] = response_value

                    # Data handling for non-nested fields of the response
                    else:
                        if item.get(columns_alias[column_name]) is not None:
                            response_value = item[columns_alias[column_name]]
                            row[column_name] = response_value

                        else:
                            row[column_name] = None

                data.append(row)
                row_index += 1

        return data


    def path(self, data_type, folder_name=None):
        """Returns the path of the dataset in the specified format in local files. If a folder is not specified, it
        returns the default path."""

        default_types_folders = {"csv": csv_default_folder_name, "json": json_default_folder_name}

        if data_type not in default_types_folders.keys():
            raise ValueError("Invalid data type, valid types are:", ", ".join(default_types_folders.keys()))

        if folder_name is None:
            folder_path = files.make_folder(default_types_folders[data_type])
        else:
            folder_path = files.make_folder(folder_name)

        file_path = folder_path + self.__name + "." + data_type

        return file_path

    # TODO: Add treatment to overwrite cards that already exist in csv by card id
    def save_csv(self, response, folder_name=None):
        """Saves the data from the provided response in a csv file."""

        data = self.parse_response(response)
        file_path = self.path("csv", folder_name)

        if data is not None:
            print(f"Saving {self.name} data in csv file locally...")
            if exists(file_path):
                df = DataFrame.from_records(data)
                df.to_csv(file_path, mode="a", index=False, header=False)
                mode_text = f"{self.name.capitalize()} data appended in csv: "
            else:
                df = DataFrame.from_records(data)
                df.to_csv(file_path, mode="w", index=False)
                mode_text = f"{self.name.capitalize()} csv saved locally as: "

            return_text = mode_text + file_path
            print(return_text)

        else:
            print("No response data to be saved in the csv file.")

    # TODO: Add treatment to overwrite cards that already exist in json by card id
    def save_json(self, response, folder_name=None):
        """Saves the data from the provided response in a json file."""

        data = self.parse_response(response)
        file_path = self.path("json", folder_name)

        if data is not None:
            print(f"Saving {self.name} data in json file locally...")
            if exists(file_path):
                df = DataFrame.from_records(data)
                df.to_json(file_path, mode="a", lines=True, orient="records")
                mode_text = f"{self.name.capitalize()} data appended in json: "
            else:
                df = DataFrame.from_records(data)
                df.to_json(file_path, mode="w", lines=True, orient="records")
                mode_text = f"{self.name.capitalize()} json saved locally as: "

            return_text = mode_text + file_path
            print(return_text)

        else:
            print("No response data to be saved in the json file.")


if __name__ == '__main__':
    pass
