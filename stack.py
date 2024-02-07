from typing import Any, Optional
from linked_list import Node, aslist


class Stack:
    root: Optional["Node"]
    __len: int = 0

    def __init__(self):
        self.root = self.tail = None
        self.__len = 0

    def pop(self):
        # o(1)
        if self.root is None:
            raise IndexError

        self.__len -= 1
        value = self.root.value
        self.root = self.root.next   # type: ignore
        return value

    def push(self, value):
        # O(1)
        new_node = Node(value)
        new_node.next = self.root   # type: ignore
        self.root = new_node
        self.__len += 1

    def __iter__(self):
        current_node = self.root
        while current_node:
            yield current_node.value  # type: ignore
            current_node = current_node.next  # type: ignore

    def __len__(self) -> int:
        return self.__len


if __name__ == '__main__':
    a = Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    print(aslist(a))
    print()
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
