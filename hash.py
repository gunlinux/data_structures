from linked_list import LinkedList
from typing import Any, Optional
import hashlib


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
            return 1

        if self.sublist is None:
            if self.key != key:
                self.sublist = LinkedList()
                self.sublist.append((self.key, self.value))
            else:
                # key already exist
                raise ValueError

            self.sublist.append((key, value))
            return 0

        for k, _ in self.sublist:
            if k == key:
                raise ValueError

        self.sublist = LinkedList()
        self.sublist.append((key, value))
        return 0

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
            if self.value is None:
                return '<>'
            return f"<{self.value}>"
        return f"<{self.value}({len(self.sublist)})>"

    def __repr__(self):
        return self.__str__()


class MyHash:
    __data: list
    __filled: int
    __size: int

    def __init__(self, max_size=64):
        self.__data = [HashNode() for _ in range(max_size)]
        self.__filled = 0
        self.__size = max_size

    def add(self, key, value):
        index = self.__hashfunc(key)
        self.__filled += self.__data[index].add_value(key, value)

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
        hash = hashlib.md5(key.encode()).hexdigest()
        hash_result = int(hash[:16], 16) % self.__size
        return hash_result

    def __str__(self):
        return f"<MyHash {self.__filled} of {self.__size}>"
