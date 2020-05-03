import pytest


from linked_list import LinkedList

# implement an algorithm which creates a linked lists of all nodes at each depth of a binary tree

from minimal_bst import create_minimal_bst, Node


def create_depth_lists(node, depth_list, prev_depth):
    if node is not None:
        current_depth = prev_depth + 1

        depth_list_length = len(depth_list)
        if depth_list_length < current_depth:
            depth_list.append(LinkedList())

        create_depth_lists(node.left, depth_list, current_depth)
        depth_list[current_depth-1].append_value(node.value)
        create_depth_lists(node.right, depth_list, current_depth)


def test_create_depth_lists():
    values = range(100)

    bst = create_minimal_bst(values, 0, len(values) - 1)

    depth_lists = []
    create_depth_lists(bst, depth_lists, 0)

    print()
    for ll in depth_lists:
        list_values = ll.get_values()
        print(*list_values)



def is_balanced(depth_lists):
    list_length = len(depth_lists)
    for i in range(list_length-1):
        ll = depth_lists[i]
        list_values = ll.get_values()

        num_nodes_if_full = 2 ** i
        if len(list_values) != num_nodes_if_full:
            return False

    return True


def test_if_is_balanced_with_balanced_tree():
    values = range(100)

    bst = create_minimal_bst(values, 0, len(values) - 1)

    depth_lists = []
    create_depth_lists(bst, depth_lists, 0)

    assert is_balanced(depth_lists)


def test_if_is_balanced_unbalanced_tree():
    values = range(8)

    bst = create_minimal_bst(values, 0, len(values) - 1)
    bst.left.left.left = Node('unbalancer')
    bst.left.left.left.left = Node('unbalancer')

    depth_lists = []
    create_depth_lists(bst, depth_lists, 0)

    assert not is_balanced(depth_lists)
