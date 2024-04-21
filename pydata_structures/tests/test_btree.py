from ..btree import Tree
import pytest


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


@pytest.fixture
def tree():
    tree = Tree()
    tree.add_leaf(50)
    tree.add_leaf(30)
    tree.add_leaf(70)
    tree.add_leaf(20)
    tree.add_leaf(40)
    tree.add_leaf(60)
    tree.add_leaf(80)
    return tree


def test_delete_leaf(tree):
    assert tree.search(20)
    assert tree.delete_leaf(20)
    assert not tree.search(20)

    assert tree.search(40)
    assert tree.delete_leaf(40)
    assert not tree.search(40)

    assert tree.search(60)
    assert tree.delete_leaf(60)
    assert not tree.search(60)

    assert tree.search(80)
    assert tree.delete_leaf(80)
    assert not tree.search(80)


def test_delete_leaf_not_exist(tree):
    assert not tree.delete_leaf(10)
    assert not tree.delete_leaf(90)


def test_delete_leaf_root(tree):
    assert tree.search(50)
    assert tree.delete_leaf(50)
    assert not tree.search(50)
    assert tree.root.value == 60 
