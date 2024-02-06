import pytest
import random
from linked_list import LinkedList, aslist

DEFAULT_TEST_ARR = [187, 6, 999, 0, -16, 2, 1, 1, 15, -5, 333]


def fill_default() -> LinkedList:
    default_linked_list = LinkedList()
    for i in DEFAULT_TEST_ARR:
        default_linked_list.append(i)
    return default_linked_list


def fill_array(array) -> LinkedList:
    linked_list = LinkedList()
    for i in array:
        linked_list.append(i)
    return linked_list


def test_basic():
    a = fill_default()
    assert aslist(a) == DEFAULT_TEST_ARR


def test_out_of_bounds():
    b = LinkedList()
    a = fill_default()
    assert len(b) == 0

    with pytest.raises(IndexError):
        b[0]
        a[0]


def test_insert():
    default_list = fill_default()
    test_list = DEFAULT_TEST_ARR[:]
    for _ in range(5):
        random_value = random.randint(0, 666)
        random_pos = random.randint(0, len(test_list))
        test_list.insert(random_pos, random_value)
        default_list.insert(random_pos, random_value)
        assert len(default_list) == len(aslist(default_list))
        assert len(default_list) == len(test_list)
    assert aslist(default_list) == test_list


def test_pop():
    default_list = fill_default()
    test_list = DEFAULT_TEST_ARR[:]
    for _ in range(len(test_list)):
        assert default_list.pop(0) == test_list.pop(0)
        assert len(default_list) == len(test_list)
        assert len(default_list) == len(aslist(default_list))

    with pytest.raises(IndexError):
        default_list.pop(0)
        test_list.pop(0)
    assert len(default_list) == 0

    default_list = fill_default()
    test_list = DEFAULT_TEST_ARR[:]
    for _ in range(5):
        rand_pos = random.randint(0, len(test_list) - 1)
        assert default_list.pop(rand_pos) == test_list.pop(rand_pos)
    assert aslist(default_list) == test_list


def test_update():
    default_list = fill_default()
    test_list = DEFAULT_TEST_ARR[:]
    for _ in range(5):
        rand_pos = random.randint(0, len(test_list) - 1)
        random_value = random.randint(0, 666)
        default_list[rand_pos] = random_value
        test_list[rand_pos] = random_value
        assert default_list[rand_pos] == test_list[rand_pos]


def test_iter():
    default_list = fill_default()
    for i, el in enumerate(default_list):
        assert default_list[i] == el


def test_search():
    default_list = fill_default()
    empty_list = LinkedList()
    test_list = DEFAULT_TEST_ARR[:]
    for el in test_list:
        assert default_list.index(el) == test_list.index(el)

    with pytest.raises(ValueError):
        default_list.index(2023)

    with pytest.raises(ValueError):
        empty_list.index(2023)
