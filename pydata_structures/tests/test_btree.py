from ..btree import Tree


def test_add_leaf():
    tree = Tree()
    tree.add_leaf(5)
    tree.add_leaf(3)
    tree.add_leaf(7)
    tree.add_leaf(7)

    # Проверяем, что дерево корректно содержит добавленные значения
    assert tree.root.value == 5
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7


def test_search():
    tree = Tree()
    tree.add_leaf(5)
    tree.add_leaf(3)
    tree.add_leaf(7)

    # Проверяем, что поиск работает правильно
    assert tree.search(3) is True
    assert tree.search(7) is True
    assert tree.search(10) is False


def test_walk():
    tree = Tree()
    test_data = [5, 3, 7, 2, 4, 6, 8]
    for el in test_data:
        tree.add_leaf(el)
    assert tree.lnr_walk() == sorted(test_data)
    assert tree.rnl_walk() == list(reversed(sorted(test_data)))
