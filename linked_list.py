from typing import Any


class Node:
    value = Any
    next = Any

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        print(f"new node {value} {next}")

    def __str__(self):
        next_value = None
        if self.next:
            next_value = self.next.value

        return f"{id(self)} {self.value} n -> {next_value}"


class LinkedList:
    root: Node | None

    def __init__(self):
        self.root = None

    def insert(self, value, index):
        node = self.root
        prev = None

        for _ in range(index):
            prev = node
            if node is None:
                raise IndexError
            node = node.next

        new_node = Node(value=value, next=node)
        if node is self.root:
            self.root = new_node
        elif prev:
            prev.next = new_node

    def delete(self, index):
        print(f"delete {index}")
        pass

    def get(self, index):
        node = self.root
        for _ in range(index):
            if node.next:
                node = node.next
            else:
                raise IndexError
        if node is None:
            raise IndexError
        return node.value

    def pop(self, index=None):
        print(f"pop {index}")
        pass

    def append(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node:
            if current_node.next is None:
                current_node.next = new_node
                return
            current_node = current_node.next

    # walktrough
    def walk(self):
        current_node = self.root
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def debug(self):
        print()
        for i in self.walk():
            print(i)


def main():
    a = LinkedList()
    for i in [187, 6, 999]:
        a.append(i)

    out = []
    for i in a.walk():
        out.append(i)
    print(out)
    print(a.get(0))
    print(a.get(1))
    print(a.get(2))
    a.debug()
    a.insert(index=3, value=3)
    a.insert(index=0, value=0)
    a.debug()


if __name__ == "__main__":
    main()
