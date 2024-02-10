import pytest
from stack import Stack


def test_basic():
    stack = Stack()
    TEST_LIST = [1, 2, 3, 4]
    for el in TEST_LIST:
        stack.push(el)
    for i, el in enumerate(reversed(TEST_LIST)):
        assert stack.pop() == el
        assert len(stack) == len(TEST_LIST) - i - 1
    assert len(stack) == 0

    with pytest.raises(IndexError):
        stack.pop()
