from typing import Any, Iterator, Optional
from .linked_list import Node


class Queue:
    def __init__(self) -> None:
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None
        self.__len = 0

    def enqueue(self, value: Any) -> None:
        self.__len += 1
        node = Node(value=value)
        if not self.head:
            self.tail = self.head = node
            return
        if self.tail:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Any:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.__len = max(self.__len - 1, 0)
            return value
        raise IndexError

    def peek(self) -> Any:
        if self.head:
            return self.head.value
        raise IndexError

    def __len__(self) -> int:
        return self.__len
