import pytest

# Write code to remove dupes from an unsorted list
# How would you do this if a buffer is not allowed?
from linked_list import LinkedList as LinkedListBase


class LinkedList(LinkedListBase):
    def remove_dups_unoptimized(self):
        current_ptr = self.head
        while current_ptr is not None:
            dup_node = self._find_next(current_ptr.next, current_ptr.value)
            while dup_node:
                self.delete_by_node(dup_node)
                dup_node = self._find_next(current_ptr.next, current_ptr.value)

            current_ptr = current_ptr.next

        return True

    def remove_dups_optimized(self):
        current_ptr = self.head
        while current_ptr is not None:
            dup_node = self._find_next(current_ptr.next, current_ptr.value)
            while dup_node:
                next_to_visit = dup_node.next
                self.delete_by_node(dup_node)
                dup_node = self._find_next(next_to_visit, current_ptr.value)

            current_ptr = current_ptr.next

        return True

    def remove_dups_buffer(self):
        current_ptr = self.head
        existing_values = {}
        while current_ptr is not None:
            if current_ptr.value in existing_values.keys():
                self.delete_by_node(current_ptr)
            else:
                existing_values[current_ptr.value] = True

            current_ptr = current_ptr.next

        return True


def test_remove_dups_buffer():
    ll = LinkedList()
    values = [3, 5, 2, 8, 7, 3, 9, 5, 3, 5]

    for v in values:
        ll.append_value(v)

    ll.remove_dups_buffer()
    ll_values = ll.get_values()

    assert len(ll_values) == len(set(values))


def test_remove_dups_optimized():
    ll = LinkedList()
    values = [3,5,2,8,7,3,9,5,3,5]

    for v in values:
        ll.append_value(v)

    ll.remove_dups_optimized()
    ll_values = ll.get_values()

    assert len(ll_values) == len(set(values))


def test_remove_dups():
    ll = LinkedList()
    values = [3,5,2,8,7,3,9,5,3,5]

    for v in values:
        ll.append_value(v)

    ll.remove_dups_unoptimized()
    ll_values = ll.get_values()

    assert len(ll_values) == len(set(values))
