from typing import Any, Optional
from .linked_list import Node


class Queue:
    def __init__(self) -> None:
        self.head: Optional["Node"] = None
        self.tail: Optional["Node"] = None
        self.__size: int = 0

    def enqueue(self, value: Any) -> None:
        self.__size += 1
        node: Node = Node(value=value)
        if not self.head:
            self.tail = self.head = node
            return
        if self.tail:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Any:
        if self.head:
            value: Any = self.head.value
            self.head = self.head.next
            self.__size -= 1
            return value
        raise IndexError

    def peek(self) -> Any:
        return self.head.value if self.head else None

    def __len__(self) -> int:
        return self.__size
