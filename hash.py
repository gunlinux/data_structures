from re import sub
from linked_list import LinkedList
from typing import Any, Optional


class HashNode:
    value: Any
    sublist: Optional[LinkedList]
    key: str

    def __init__(self):
        self.value = None
        self.sublist = None

    def set_value(self, key, value):
        # if only one
        if self.value is None:
            self.value = value
            self.key = key
            return

        if self.sublist is None:
            if self.key != key:
                self.sublist = LinkedList()
                print(f'added current {self.key} {self.value}')
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
        self.__data[index].set_value(key, value)
        print(self.__data[index])

    def get(self, key, default=None):
        index = self.__hashfunc(key)
        val = self.__data[index].get_value(key, default)
        return val

    def __hashfunc(self, key):
        return len(key)


def main() -> None:
    phonebook = MyHash(max_size=15)
    phonebook.add("loki", "1999")

    phonebook.add("olegan", "2000")
    phonebook.add("petr", "1000")
    phonebook.get("loki")
    phonebook.get("petr")

if __name__ == "__main__":
    main()
