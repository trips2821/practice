import pytest

from stack import Node, Stack, StackEmptyException


def test_is_empty_empty_stack():
    s = Stack()
    assert s.is_empty()


def test_is_empty_not_empty_stack():
    s = Stack()
    value = 1
    n = Node(value)
    s.top = n

    assert not s.is_empty()


def test_push():
    s = Stack()
    value = 1
    s.push(value)

    assert s.top.value == value


def test_push_multiple():
    s = Stack()
    values = [1,2,3,]

    for v in values:
        s.push(v)

    assert s.top.value == values[-1]
    assert s.top.next.value == values[-2]


def test_pop():
    s = Stack()
    value = 1
    s.push(value)

    popped_value = s.pop()

    assert popped_value == value


def test_pop_empty_raises_error():
    s = Stack()
    with pytest.raises(StackEmptyException):
        s.pop()


def test_pop_all_plus_one_raises_error():
    s = Stack()
    value = 1
    s.push(value)

    s.pop()
    with pytest.raises(StackEmptyException):
        s.pop()


def test_peek():
    s = Stack()
    value = 1
    s.push(value)

    peeked_value = s.peek()

    assert peeked_value == value
    assert not s.is_empty()
