from collections.abc import Iterable
from typing import Any, Optional
import copy


class Node:
    value = Any
    next = Optional["Node"]

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} {str(self.next)}"


class LinkedList:
    root: Optional["Node"]
    tail: Optional["Node"]
    __len: int = 0

    def __init__(self):
        self.root = self.tail = None
        self.__len = 0

    def insert(self, index: int, value: Any):
        # O(n)
        node: Optional["Node"] = self.root
        prev = None

        for _ in range(index):
            prev = node
            if not isinstance(node, Node):
                raise IndexError
            node = node.next  # type: ignore

        new_node = Node(value=value)
        self.__len += 1
        new_node.next = node  # type: ignore
        if node is self.root:
            self.root = new_node
        elif prev:
            prev.next = new_node  # type: ignore

    def __get(self, index: int) -> Any:
        #  O(n)
        node, _ = self.__get_node_by_index(index)
        return node

    def __get_node_by_index(self, index: int):
        node: Optional[Node] = self.root
        prev: Optional[Node] = None
        if node is None:
            raise IndexError
        for _ in range(index):
            if isinstance(node, Node):
                prev = node  # type: ignore
                node = node.next  # type: ignore
            else:
                raise IndexError
        return node, prev  # type: ignore

    def pop(self, index: int):
        # o(n)
        node, prev = self.__get_node_by_index(index)
        self.__len -= 1
        if prev is None:
            value = copy.deepcopy(self.root.value)   # type: ignore
            self.root = self.root.next     # type: ignore
            return value
        if node:
            value = copy.deepcopy(node.value)  # type: ignore
            prev.next = node.next              # type: ignore
            return value
        raise IndexError

    def index(self, value=Any) -> int:
        # O(n)
        for index, el in enumerate(self):
            if el == value:
                return index
        raise ValueError

    def append(self, value):
        # O(1)
        new_node = Node(value)
        self.__len += 1

        if self.root is None:
            self.root = self.tail = new_node
            return

        if self.root.next is None:
            self.tail = new_node
            self.root.next = self.tail   # type: ignore
            return

        self.tail.next = new_node   # type: ignore
        self.tail = new_node

    def __iter__(self):
        current_node = self.root
        while current_node:
            yield current_node.value  # type: ignore
            current_node = current_node.next  # type: ignore

    def __getitem__(self, index:  int) -> Any:
        return self.__get(index=index).value

    def __setitem__(self, index: int, value: Any) -> None:
        item_to_update = self.__get(index=index)
        item_to_update.value = value

    def __len__(self) -> int:
        return self.__len


def aslist(linked_list: Iterable) -> list:
    return [i for i in linked_list]


def find_min(linked_list: LinkedList) -> tuple[int, Any]:
    min_el = linked_list[0]
    min_pos = 0
    for i, el in enumerate(linked_list):
        if el < min_el:
            min_el = el
            min_pos = i
    return (min_pos, min_el)


def min_sort(linked_list: LinkedList) -> LinkedList:
    if not len(linked_list):
        return linked_list
    start_len = len(linked_list)
    out_list = copy.deepcopy(LinkedList())
    for _ in range(start_len):
        min_pos, _ = find_min(linked_list)
        out_list.append(linked_list.pop(min_pos))
    return out_list
