from src.repository.repository import Repository
import pickle


class BinaryRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    @property
    def binary_data(self):
        return super().data

    @binary_data.setter
    def binary_data(self, value):
        self.data = value

    def __read_entities(self):
        with open(self._file_name, "rb") as f:
            try:
                lis = pickle.load(f)
                for elem in lis:
                    super().add_item(elem)
            except EOFError:
                pass

    def __update_file(self):
        with open(self._file_name, "wb") as f:
            pickle.dump(self.binary_data, f)
            self.binary_data.clear()

    def add_item(self, obj):
        self.__read_entities()
        super().add_item(obj)
        self.__update_file()

    def __getitem__(self, item):
        self.__read_entities()
        i = super().__getitem__(item)
        self.data.clear()
        return i

    def __setitem__(self, index, item):
        self.__read_entities()
        super().__setitem__(index, item)
        self.__update_file()

    def __delitem__(self, index):
        self.__read_entities()
        super().__delitem__(index)
        self.__update_file()

    def __str__(self):
        self.__read_entities()
        r = super().__str__()
        self.__update_file()
        return r


# FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK
# :( :( :( :( :( :( :( :(