import pytest

# Write a func to delete a middle node (not the first or last node) in a linked list

from linked_list import LinkedList as LinkedListBase

class LinkedList(LinkedListBase):
    def delete_node_in_place(self, node):
        node.value = node.next.value

        node_to_delete = node.next
        node.next = node_to_delete.next

        del node_to_delete

def test_delete_node_in_place():
    ll = LinkedList()
    values = [1, 2, 3]

    for v in values:
        ll.append_value(v)

    middle_node_value_index = 1
    node_to_delete = ll.find_by_value(values[middle_node_value_index])
    ll.delete_node_in_place(node_to_delete)
    ll_values = ll.get_values()

    expected_values = values[:middle_node_value_index] + values[middle_node_value_index+1:]
    assert ll_values == expected_values
