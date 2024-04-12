from typing import Optional, Any
from collections import deque
import random


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.value})'

    def __repr__(self):
        return f'Node({self.value})'


class Tree:
    def __init__(self):
        self.root = None

    def add_leaf(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def add_leaf_inner(root, value):
            if root and root.value > value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    add_leaf_inner(root=root.left, value=value)
                return

            if root and root.value < value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    add_leaf_inner(root=root.right, value=value)
                return
        return add_leaf_inner(self.root, value)

    def lnr_walk(self) -> None:
        def walk(root: Optional[Node]) -> None:
            if root is None:
                return
            walk(root.left)
            print(root.value)
            walk(root.right)

        return walk(self.root)

    def rnl_walk(self) -> None:
        def walk(root: Optional[Node]) -> None:
            if root is None:
                return
            walk(root.right)
            print(root.value)
            walk(root.left)

        return walk(self.root)

    def nlr_walk(self) -> None:
        def walk(root: Optional[Node]) -> None:
            if root is None:
                return
            print(root.value)
            walk(root.left)
            walk(root.right)

        return walk(self.root)

    def bsf_walk(self):
        level = 0
        current_level = [self.root]
        while any(current_level):
            next_level = []
            level += 1
            self.__render_level(level, current_level)
            for node in current_level:
                if node:
                    next_level.extend([node.left, node.right])
                else:
                    next_level.append(None)
                    next_level.append(None)
            current_level = next_level

    def __render_level(self, level, items, max_len=60):
        step_count = ((max_len-10*(level+1))//2)
        temp = ' '.join([f'{str(x if x else " "):5}' for x in items])
        print(f"{' '*step_count}{temp}")
        print()

    def search(self, find_value: Any) -> bool:
        def inner_search(root, find_value):
            if root is None:
                return False

            if root.value == find_value:
                return True

            if root.value > find_value and root.left:
                return inner_search(root.left, find_value)

            if root.value < find_value and root.right:
                return inner_search(root.right, find_value)
            return False
        return inner_search(self.root, find_value)

    def print_tree_to_console(self) -> None:
        """Выводит красиво отформатированное бинарное дерево в консоль. gpt meh :D"""
        # Проверяем, есть ли корневой узел
        if self.root is None:
            print("Tree is empty")
            return

        # Рекурсивный метод для красивого вывода дерева
        def display(root, space=0, level_spacing=4):
            if root is None:
                return

            # Добавляем отступ в зависимости от уровня дерева
            space += level_spacing

            display(root.right, space)

            print(" " * space, str(root.value))

            display(root.left, space)

        # Вызов рекурсивного метода для корневого узла
        display(self.root)


def main():
    '''
    test tree
       5
    /     |
    3        9
    /  |   /   |
    1   4   6  11
    '''
    root = Tree()
    root.add_leaf(5)
    root.add_leaf(3)
    root.add_leaf(1)
    root.add_leaf(4)
    root.lnr_walk()
    root.print_tree_to_console()
    return


if __name__ == "__main__":
    main()
