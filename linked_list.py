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

    def __init__(self):
        self.root = None

    def insert(self, value, index):
        node: Optional["Node"] = self.root
        prev = None

        for _ in range(index):
            prev = node
            if not isinstance(node, Node):
                raise IndexError
            node = node.next  # type: ignore

        new_node = Node(value=value)
        new_node.next = node  # type: ignore
        if node is self.root:
            self.root = new_node
        elif prev:
            prev.next = new_node  # type: ignore

    def update(self, index, value=None):
        print(f'TODO: not implemented update {index} {value}')
        raise NotImplementedError

    def get(self, index: int) -> Any:
        node, _ = self.__get_node_by_index(index)
        return node.value   # type: ignore

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
        node, prev = self.__get_node_by_index(index)
        if prev is None:
            value = copy.deepcopy(self.root.value)   # type: ignore
            self.root = self.root.next     # type: ignore
            return value
        if node:
            value = copy.deepcopy(node.value)  # type: ignore
            prev.next = node.next              # type: ignore
            return value
        raise IndexError

    def append(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current_node: Node = self.root
        while current_node:
            if current_node.next is None:
                current_node.next = new_node  # type: ignore
                return
            current_node = current_node.next  # type: ignore

    # walktrough
    def walk(self):
        current_node = self.root
        while current_node:
            yield current_node.value  # type: ignore
            current_node = current_node.next  # type: ignore

    def __getitem__(self, index:  int) -> Any:
        return self.get(index=index)

    def debug(self):
        print()
        for i in self.walk():
            print(i)


def aslist(linked_list: LinkedList) -> list:
    return [i for i in linked_list.walk()]
