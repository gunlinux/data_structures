import pytest
from ..queue import Queue


def test_basic():
    queue = Queue()
    queue.enqueue(1)
    assert len(queue) == 1
    assert 1 == queue.peek()
    assert 1 == queue.dequeue()
    assert len(queue) == 0
    queue.enqueue(2)
    assert len(queue) == 1
    queue.enqueue(3)
    assert len(queue) == 2
    assert 2 == queue.dequeue()
    assert len(queue) == 1
    assert 3 == queue.dequeue()
    assert len(queue) == 0
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()

    for i in range(1, 20):
        queue.enqueue(i)
    for i in range(1, 20, -1):
        assert i == queue.dequeue()
