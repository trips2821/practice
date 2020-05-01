import pytest

# find the Kth to the last element in a singly linked list

from linked_list import LinkedList as LinkedListBase


# O(n)th solution

class LinkedList(LinkedListBase):
    counter = 0
    depth = 1
    def get_kth_to_last_element(self, node, kth):
        if node.next is not None:
            self.counter += 1
            self.depth += 1
            n = self.get_kth_to_last_element(node.next, kth)
            if n is None:
                n = node if self.counter == self.depth - kth else None
            self.counter -= 1
            return n
        else:
            return


def test_get_kth_to_last_element():
    ll = LinkedList()
    values = [1,2,3,4,5,6,7,8,9]

    for v in values:
        ll.append_value(v)

    kth = 2
    kth_node_value = values[-kth - 1]

    got_node = ll.get_kth_to_last_element(ll.head, kth)

    expected_node = ll.find_by_value(kth_node_value)
    assert got_node is expected_node
