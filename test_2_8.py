import pytest

# Find loop connection in a singly linked list

from linked_list import LinkedList as LinkedListBase


def find_loop(link_list):
    slow_ptr = link_list.head
    fast_ptr = link_list.head

    while True:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr is slow_ptr:
            print(fast_ptr.value, slow_ptr.value)
            break

    slow_ptr = link_list.head
    while True:
        fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next
        if slow_ptr is fast_ptr:
            break

    return slow_ptr


def test_find_loop():
    ll = LinkedListBase()
    values = [1,2,3,4,5,6,7,8,9]

    for v in values:
        ll.append_value(v)

    tail = ll.find_by_value(values[-1])
    looped_node = ll.find_by_value(2)
    tail.next = looped_node

    found_node = find_loop(ll)
    assert found_node is looped_node
