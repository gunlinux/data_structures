from linked_list import LinkedList
import hashlib


class HashNode:
    def __init__(self):
        self.sublist: LinkedList = LinkedList()

    def add_value(self, key, value):
        for k, _ in self.sublist:
            if k == key:
                raise ValueError

        self.sublist.append((key, value))
        return 1

    def set_value(self, key, value):
        for index, item in enumerate(self.sublist):
            k, _ = item
            if k == key:
                self.sublist[index] = key, value

    def get_value(self, key: str):
        if len(self.sublist) == 1:
            return self.sublist.get(0)[1]

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

    def keys(self):
        if self.sublist:
            return [item[0] for item in self.sublist]

    def values(self):
        if self.sublist:
            return [item[1] for item in self.sublist]

    def __str__(self):
        values = ",".join([x[0] for x in self.sublist])
        return f"({len(self.sublist)}) {values}>"

    def __repr__(self):
        return self.__str__()


class MyHash:
    def __init__(self, max_size=64):
        self.__data: list = [None] * max_size
        self.__filled: int = 0
        self.__size: int = max_size

    def add(self, key, value):
        index = self.__hashfunc(key)
        if self.__data[index] is None:
            self.__data[index] = HashNode()
            self.__filled += self.__data[index].add_value(key, value)
            return
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
        val, c = self.__data[index].pop_key(key)
        self.__filled -= c
        return val

    def __hashfunc(self, key):
        return self.__hashcalc(key) % self.__size

    def __hashcalc(self, key):
        hash = hashlib.md5(key.encode()).hexdigest()
        return int(hash[:16], 16)

    def __str__(self):
        return f"<MyHash {self.__filled} of {self.__size}>"

    def keys(self):
        return [x for c in self.__data if c is not None for x in c.keys()]

    def values(self):
        return [x for c in self.__data if c is not None for x in c.values()]

    def __rehash__(self):
        pass

    def __resize__(self):
        pass

    def __len__(self):
        return self.__filled

    def debug(self):
        for el in self.__data:
            print(el)
