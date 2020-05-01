import pytest

# Partition a linked list around a value x so that all nodes that come before it an in one list
# and all node that come after it are in another, lists should be ordered

from linked_list import LinkedList as LinkedListBase, Node


class LinkedList(LinkedListBase):
    def pop_node(self, node):
        new_node = Node(node.value)

        if node.next is not None:
            node.value = node.next.value
            node.next = node.next.next
        else:
            self.delete_by_node(node)

        return new_node


def partition_list(linked_list, value):
    less_than = LinkedList()
    greater_than_or_equal_to = LinkedList()
    head = linked_list.head

    while head is not None:
        node = linked_list.pop_node(head)
        if node.value < value:
            less_than.append_node(node)
        else:
            greater_than_or_equal_to.append_node(node)

        head = linked_list.head

    current_ptr = less_than.head
    while current_ptr.next is not None:
        current_ptr = current_ptr.next

    current_ptr.next = greater_than_or_equal_to.head
    greater_than_or_equal_to.head = None

    return less_than

def test_partition_list():
    ll = LinkedList()
    values = [3,5,8,5,10,2,1]

    for v in values:
        ll.append_value(v)

    partitioned_list = partition_list(ll, 5)

    expected_values = [3,2,1,5,8,5,10]

    assert partitioned_list.get_values() == expected_values


def test_pop_all_nodes():
    ll = LinkedList()
    values = [1, 2, 3]

    for v in values:
        ll.append_value(v)

    for i in range(len(values)):
        node = ll.pop_node(ll.head)
        assert node.value == values[i]

    assert ll.head is None


def test_pop_middle_node():
    ll = LinkedList()
    values = [1, 2, 3]

    for v in values:
        ll.append_value(v)

    value_to_pop_index = 1
    value_to_pop = values[value_to_pop_index]
    node_to_pop = ll.find_by_value(value_to_pop)

    popped_node = ll.pop_node(node_to_pop)

    expected_values = values[:value_to_pop_index] + values[value_to_pop_index+1:]

    assert ll.get_values() == expected_values


def test_pop_first_node():
    ll = LinkedList()
    values = [1, 2, 3]

    for v in values:
        ll.append_value(v)

    value_to_pop_index = 0
    value_to_pop = values[value_to_pop_index]
    node_to_pop = ll.find_by_value(value_to_pop)

    popped_node = ll.pop_node(node_to_pop)

    expected_values = values[:value_to_pop_index] + values[value_to_pop_index+1:]

    assert ll.get_values() == expected_values

def test_pop_last_node():
    ll = LinkedList()
    values = [1, 2, 3]

    for v in values:
        ll.append_value(v)

    value_to_pop_index = -1
    value_to_pop = values[value_to_pop_index]
    node_to_pop = ll.find_by_value(value_to_pop)

    popped_node = ll.pop_node(node_to_pop)

    expected_values = values[:value_to_pop_index]

    assert ll.get_values() == expected_values
