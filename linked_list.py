from collections.abc import Iterable
from typing import Any, Optional
import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional["Node"] = None

    def __str__(self):
        return f"{self.value} {str(self.next)}"


class LinkedList:
    def __init__(self):
        self.root: Optional["Node"] = None
        self.tail: Optional["Node"] = None
        self.__len = 0

    def insert(self, index: int, value: Any):
        # O(n)
        node: Optional["Node"] = self.root
        prev = None

        for _ in range(index):
            prev = node
            if not isinstance(node, Node):
                raise IndexError
            node = node.next

        new_node = Node(value=value)
        self.__len += 1
        new_node.next = node
        if node is self.root:
            self.root = new_node
        elif prev:
            prev.next = new_node

    def __get(self, index: int) -> Any:
        #  O(n)
        node, _ = self.__get_node_by_index(index)
        return node

    def get(self, index: int) -> Any:
        return self.__get(index=index).value

    def __get_node_by_index(self, index: int):
        node: Optional[Node] = self.root
        prev: Optional[Node] = None
        if node is None:
            raise IndexError
        for _ in range(index):
            if isinstance(node, Node):
                prev = node
                node = node.next
            else:
                raise IndexError
        return node, prev

    def pop(self, index: int = 0):
        # o(n)
        node, prev = self.__get_node_by_index(index)
        self.__len -= 1
        if prev is None and self.root is not None:
            value = copy.deepcopy(self.root.value)
            self.root = self.root.next
            return value
        if node and prev is not None:
            value = copy.deepcopy(node.value)
            prev.next = node.next
            return value
        raise IndexError

    def index(self, value: Any) -> int:
        # O(n)
        for index, el in enumerate(self):
            if el == value:
                return index
        raise ValueError

    def append(self, value: Any):
        # O(1)
        new_node = Node(value)
        self.__len += 1

        if self.root is None:
            self.root = self.tail = new_node
            return

        if self.root.next is None:
            self.tail = new_node
            self.root.next = self.tail
            return
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

    def __iter__(self):
        current_node = self.root
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __getitem__(self, index: int) -> Any:
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
