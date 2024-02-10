from linked_list import LinkedList
from typing import Any, Optional


class HashNode:
    value: Any
    sublist: Optional[LinkedList]
    key: str

    def __init__(self):
        self.value = None
        self.sublist = None

    def add_value(self, key, value):
        # if only one
        if self.value is None:
            self.value = value
            self.key = key
            return

        if self.sublist is None:
            if self.key != key:
                self.sublist = LinkedList()
                self.sublist.append((self.key, self.value))
            else:
                raise ValueError

            self.sublist.append((key, value))
            return

        for k, _ in self.sublist:
            if k == key:
                raise ValueError

        self.sublist = LinkedList()
        self.sublist.append((key, value))

    def set_value(self, key, value):
        if self.sublist is None:
            self.value = value
            return

        for index, item in enumerate(self.sublist):
            k, _ = item
            if k == key:
                self.sublist[index] = key, value

    def get_value(self, key: str):
        if self.sublist is None:
            if self.value is None:
                raise ValueError

            return self.value

        for k, v in self.sublist:
            if k == key:
                return v
        raise ValueError

    def pop_key(self, key: str):
        if self.sublist is None:
            if self.value is None:
                raise ValueError
            copy = self.value
            self.value = None
            return copy

        for index, item in enumerate(self.sublist):
            k, v = item
            if k == key:
                self.sublist.pop(index)
                return v

    def __str__(self):
        if self.sublist is None:
            return f"<{self.value}"
        return f"<{self.value} {len(self.sublist)}>"


class MyHash:
    __data: list

    def __init__(self, max_size=6):
        self.__data = [HashNode() for _ in range(max_size)]

    def add(self, key, value):
        index = self.__hashfunc(key)
        self.__data[index].add_value(key, value)
        print(self.__data[index])

    def seti(self, key, value):
        index = self.__hashfunc(key)
        self.__data[index].set_value(key, value)
        return

    def get(self, key):
        index = self.__hashfunc(key)
        val = self.__data[index].get_value(key)
        return val

    def pop(self, key):
        index = self.__hashfunc(key)
        val = self.__data[index].pop_key(key)
        return val

    def __hashfunc(self, key):
        return len(key)
