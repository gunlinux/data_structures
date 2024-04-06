from typing import Any


class ArrayBuffer:
    def __init__(self, cap=10):
        self.__cap: int = cap
        self.__size: int = 0
        self.__data: list[Any] = [0] * self.__cap
        self.__head = self.__tail = cap // 3

    def append(self, item: Any):
        if self.__size and self.__head == self.__tail:
            self.__resize()
        self.__data[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__cap
        self.__size += 1

    def __resize(self):
        new_cap = self.__cap * 2
        self.__newdata: list[Any] = [0] * new_cap
        head = tail = new_cap // 3
        for i in range(self.__head, self.__head + self.__size):
            self.__newdata[tail % new_cap] = self.__data[i % self.__cap]
            tail += 1
        self.__head = head
        self.__data = self.__newdata
        self.__cap = new_cap
        self.__tail = tail % self.__cap
        print('resize here')

    @property
    def data(self) -> str:
        return ",".join([str(x) for x in self.__data])

    def __str__(self) -> str:
        return f'c: {self.__cap}, h: {self.__head}, t: {self.__tail}, s: {self.__size}'


if __name__ == "__main__":
    arr = ArrayBuffer(cap=5)
    for i in range(1, 10):
        print(arr)
        arr.append(i)
