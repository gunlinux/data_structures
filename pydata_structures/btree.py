from typing import Optional, Any, List


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value: Any = value
        self.left: Optional["Node"] = left
        self.right: Optional["Node"] = right

    def childs_count(self) -> int:
        return bool(self.left) + bool(self.right)

    def __str__(self) -> str:
        return f'Node({self.value})'

    def __repr__(self) -> str:
        return f'Node({self.value})'


class Tree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def add_leaf(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def add_leaf_inner(root: Optional[Node], value) -> None:
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

    def delete_leaf(self, value: Any) -> bool:

        def subdelete(parent: Optional[Node], to_kill: Node, right=False):
            childs = to_kill.childs_count()
            if not childs:
                if parent:
                    if right:
                        parent.right = None
                    else:
                        parent.left = None
                else:
                    #  Если удаляем узел корень и единственный
                    parent = None
                    self.root = None

            if childs == 1:
                child = to_kill.right if to_kill.right else to_kill.left
                if parent:
                    if right:
                        parent.right = child
                    else:
                        parent.left = child
                else:
                    self.root = child

            if childs == 2:
                #  Много потомков
                print(f'find lowest on {to_kill.right}')
                lowest = self.find_lowest(to_kill.right, to_kill)
                to_kill.value = lowest

        def walk(root: Optional[Node], value: Any) -> None:
            if root is None:
                return

            if root.value == value:
                subdelete(parent=None, to_kill=root)
                print('gotcha')

            if root.value and value > root.value and root.right:
                if root.right.value == value:
                    subdelete(root, root.right, right=True)
                    return
                walk(root.right, value)

            if root.value and value < root.value and root.left:
                if root.left.value == value:
                    subdelete(root, root.left)
                    return
                walk(root.left, value)
            pass
        walk(self.root, value)
        return False

    def lnr_walk(self) -> List[Any]:
        out: List[Any] = []

        def walk(root: Optional[Node]) -> None:
            nonlocal out
            if root is None:
                return
            walk(root.left)
            out.append(root.value)
            walk(root.right)
        walk(self.root)
        return out

    def find_lowest(self, root: Optional[Node], parent: Node) -> Any:
        out: Optional[Node] = None

        def walk(root: Optional[Node]) -> None:
            nonlocal out
            if root is None:
                return
            if root.childs_count() == 0:
                out = root.value
                parent.right = None
                return
            if root.left and not root.left.left:
                out = root.left.value
                if root.left.right:
                    root.left = root.left.right
                else:
                    root.left = None
                return
            walk(root.left)
        walk(root)
        return out

    def rnl_walk(self) -> List[Any]:
        out: List[Any] = []

        def walk(root: Optional[Node]) -> None:
            nonlocal out
            if root is None:
                return
            walk(root.right)
            out.append(root.value)
            walk(root.left)

        walk(self.root)
        return out

    def nlr_walk(self) -> List[Any]:
        out: List[Any] = []

        def walk(root: Optional[Node]) -> None:
            if root is None:
                return
            print(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return out

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

    def __render_level(self, level: int, items: List[Optional[Node]], max_len=60):
        step_count = ((max_len-10*(level+1))//2)
        temp = ' '.join([f'{str(x if x else " "):5}' for x in items])
        print(f"{' '*step_count}{temp}")
        print()

    def search(self, find_value: Any) -> bool:
        def inner_search(root: Optional[Node], find_value: Any):
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


if __name__ == '__main__':
    tree = Tree()
    test_data = [5, 3, 7, 2, 4, 6, 8, 12, 15, 13,14, 16, 18, 22, 24, 17]
    for el in test_data:
        tree.add_leaf(el)
    tree.print_tree_to_console()
    tree.delete_leaf(12)
    tree.print_tree_to_console()
