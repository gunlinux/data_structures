from .linked_list import LinkedList
from collections import namedtuple
from typing import Any
import zlib


Item = namedtuple('Item', 'key value')


class HashNode:
    def __init__(self) -> None:
        self.sublist: LinkedList = LinkedList()

    def add_value(self, key: str, value: Any) -> int:
        for k, _ in self.sublist:
            if k == key:
                raise ValueError
        self.sublist.append(Item(key, value))
        return 1

    def set_value(self, key: str, value: Any) -> None:
        for index, item in enumerate(self.sublist):
            if item.key == key:
                self.sublist[index] = Item(key, value)

    def get_value(self, key: str) -> Any:
        if len(self.sublist) == 1:
            return self.sublist.get(0).value

        for k, v in self.sublist:
            if k == key:
                return v
        raise ValueError

    def pop_key(self, key: str):
        for index, item in enumerate(self.sublist):
            k, v = item
            if k == key:
                self.sublist.pop(index)
                return v, 1
        return None, 0

    def keys(self) -> list[str]:
        if self.sublist:
            return [item.key for item in self.sublist]
        return []

    def values(self) -> list[Any]:
        if self.sublist:
            return [item.value for item in self.sublist]
        return []

    def items(self) -> list[tuple[str, Any]]:
        if self.sublist:
            return [item for item in self.sublist]
        return []

    def __str__(self) -> str:
        values = ",".join([x[0] for x in self.sublist])
        return f"({len(self.sublist)}) {values}>"

    def __repr__(self) -> str:
        return self.__str__()


class MyHash:
    def __init__(self, max_size: int = 64, threshold: float = 0.7) -> None:
        self.__data: list = [None] * max_size
        self.__filled: int = 0
        self.__size: int = max_size
        self.__threshold = threshold

    def add(self, key: str, value: Any, data=None) -> None:
        if self.__overload__() and not data:
            self.__resize__()

        if not data:
            data = self.__data

        index = self.__hashfunc(key, len(data))
        if data[index] is None:
            data[index] = HashNode()
        self.__filled += data[index].add_value(key, value)

    def seti(self, key: str, value: Any) -> None:
        index = self.__hashfunc(key)
        self.__data[index].set_value(key, value)

    def get(self, key: str) -> Any:
        index = self.__hashfunc(key)
        val = self.__data[index].get_value(key)
        return val

    def pop(self, key: str) -> Any:
        index = self.__hashfunc(key)
        val, c = self.__data[index].pop_key(key)
        self.__filled -= c
        return val

    def __hashfunc(self, key: str, size=None) -> int:
        if size is None:
            return self.__hashcalc(key) % self.__size
        return self.__hashcalc(key) % size

    def __hashcalc(self, key: str) -> int:
        return zlib.crc32(key.encode())

    def __str__(self) -> str:
        return f"<MyHash {self.__filled} of {self.__size}>"

    def keys(self) -> list[str]:
        return [x for c in self.__data if c is not None for x in c.keys()]

    def values(self) -> list[Any]:
        return [x for c in self.__data if c is not None for x in c.values()]

    def items(self) -> list[tuple[str, Any]]:
        return [x for c in self.__data if c is not None for x in c.items()]

    def __resize__(self) -> None:
        new_size = self.__size * 2
        new_data: list[HashNode | None] = [None] * new_size

        old_filled = self.__filled

        for k, v in self.items():
            self.add(key=k, value=v, data=new_data)
        self.__data = new_data
        self.__size = new_size

        self.__filled = old_filled

    def __len__(self) -> int:
        return self.__filled

    def __overload__(self) -> bool:
        return (self.__filled / self.__size) > self.__threshold

    def debug(self) -> None:
        for el in self.__data:
            print(el)
