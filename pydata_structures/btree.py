from typing import Optional, Any


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.value})'


def add_leaf(value: Any, root: Optional[Node] = None):
    if root is None:
        return Node(value=value)

    if root.value > value:
        if root.left is None:
            root.left = Node(value)
        else:
            add_leaf(root=root.left, value=value)
        return

    if root.value < value:
        if root.right is None:
            root.right = Node(value)
        else:
            add_leaf(root=root.right, value=value)
        return


def lnr_walk(root: Optional[Node]) -> None:
    if root is None:
        return
    lnr_walk(root.left)
    print(root.value)
    lnr_walk(root.right)


def rnl_walk(root: Optional[Node]) -> None:
    if root is None:
        return
    rnl_walk(root.right)
    print(root.value)
    rnl_walk(root.left)


def nlr_walk(root: Optional[Node]) -> None:
    if root is None:
        return
    print(root.value)
    nlr_walk(root.left)
    nlr_walk(root.right)


def main():
    '''
    test tree
       5
    /     |
    3        9
    /  |   /   |
    1   4   6  11
    '''
    root = Node(value=5)
    add_leaf(root=root, value=3)
    add_leaf(root=root, value=9)
    add_leaf(root=root, value=1)
    add_leaf(root=root, value=4)
    add_leaf(root=root, value=6)
    add_leaf(root=root, value=11)
    print()
    lnr_walk(root)
    print()
    rnl_walk(root)
    print()
    nlr_walk(root)
    return


if __name__ == "__main__":
    main()
