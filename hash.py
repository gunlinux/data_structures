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
                print(f"added current {self.key} {self.value}")
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

    def get_value(self, key: str, default=None):
        if self.value is None:
            return default

        if self.sublist is None:
            return self.value

        for k, v in self.sublist:
            print(k, v)
            if k == key:
                return v
        return default

    def __str__(self):
        return f"<{self.value}>"


class MyHash:
    __data: list

    def __init__(self, max_size=100):
        self.__data = [HashNode() for _ in range(max_size)]

    def add(self, key, value):
        print(f"add: {key}, {value}")
        index = self.__hashfunc(key)
        self.__data[index].add_value(key, value)
        print(self.__data[index])

    def seti(self, key, value):
        print(f"add: {key}, {value}")
        index = self.__hashfunc(key)
        self.__data[index].set_value(key, value)
        print(self.__data[index])
        return

    def get(self, key, default=None):
        index = self.__hashfunc(key)
        val = self.__data[index].get_value(key, default)
        return val

    def __hashfunc(self, key):
        return len(key)
