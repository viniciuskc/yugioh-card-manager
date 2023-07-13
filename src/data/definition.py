class Column:
    def __init__(self, name, data_type, primary_key=False, nullable=True, array=False, options=None, description=None):

        if primary_key:
            nullable = False

        self.__name = name
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
        """Returns a list with all dataset columns of the dataset sorted by name."""
        column_list = []
        for column in self.__columns:
            column_list += [column.name]
        column_list.sort()
        return column_list

    def primary_keys(self):
        """Returns a list with all primary key columns of the dataset sorted by name."""
        pk_list = []
        for column in self.__columns:
            if column.primary_key:
                pk_list += [column.name]
        pk_list.sort()
        return pk_list


if __name__ == '__main__':
    pass
