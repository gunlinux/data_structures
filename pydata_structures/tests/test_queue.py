import pytest
from ..queue import Queue


def test_enqueue_and_dequeue():
    # Создание очереди и добавление элементов
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Проверка правильности удаления элементов
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_empty_queue():
    # Проверка поведения при попытке удалить элемент из пустой очереди
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

    # Проверка наличия элементов в пустой очереди
    assert queue.peek() is None


def test_queue_length():
    # Проверка правильности вычисления длины очереди
    queue = Queue()
    assert len(queue) == 0

    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2

    queue.dequeue()
    assert len(queue) == 1


def test_dequeue_and_peek():
    # Проверка корректности работы dequeue и peek в разных сценариях
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.peek() == 2
    assert queue.dequeue() == 2
    assert queue.peek() == 3
    assert queue.dequeue() == 3
    assert queue.peek() is None
