from linked_list import LinkedList
from typing import Any, Optional
import hashlib


class HashNode:
    value: Any
    sublist: Optional[LinkedList]
    key: Optional[str]

    def __init__(self):
        self.value = None
        self.sublist = None
        self.key = None

    def add_value(self, key, value):
        # if empty  node
        if self.key is None and self.sublist is None:
            self.value = value
            self.key = key
            return 1

        if self.sublist is None:
            # if first collision
            if key == self.key:
                raise ValueError
            self.sublist = LinkedList()
            self.sublist.append((self.key, self.value))
            self.sublist.append((key, value))
            self.key = None
            self.value = None
            return 0

        for k, _ in self.sublist:
            if k == key:
                raise ValueError

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
            self.key = None
            return copy

        for index, item in enumerate(self.sublist):
            k, v = item
            if k == key:
                self.sublist.pop(index)
                return v

    def keys(self):
        if self.sublist:
            for item in self.sublist:
                print(item)
            return [item[0] for item in self.sublist]
        return [self.key] if self.key is not None else []

    def values(self):
        if self.sublist:
            return [item[1] for item in self.sublist]
        return [self.value] if self.value is not None else []

    def __str__(self):
        if self.sublist is None:
            if self.value is None:
                return "<>"
            return f"<{self.key}>"
        values =  ','.join([x[0] for x in self.sublist])
        return f"<{self.key} ({len(self.sublist)}) {values}>"

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
        print(f'hash: {key} {hash_result}')
        return hash_result

    def __str__(self):
        return f"<MyHash {self.__filled} of {self.__size}>"

    def keys(self):
        return [x for c in self.__data for x in c.keys()]

    def values(self):
        return [x for c in self.__data for x in c.values()]

    def __rehash__(self):
        pass

    def __resize__(self):
        pass

    def debug(self):
        for el in self.__data:
            print(el)
