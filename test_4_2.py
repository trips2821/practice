import pytest

import math


# Given and ordered array, write a func that generates a binary search tree of minimal height

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_minimal_bst(values, start_index, end_index):
    mid_index = (start_index + end_index ) // 2

    node_value = values[mid_index]
    node = Node(node_value)

    if end_index == start_index:
        return node

    if end_index < start_index:
        return None

    node.left = create_minimal_bst(values, start_index, mid_index - 1)
    node.right = create_minimal_bst(values, mid_index + 1, end_index)

    return node


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def pre_order(node):
    if node is not None:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


def test_create_minimal_bst():
    values = range(13)

    bst = create_minimal_bst(values, 0, len(values) - 1)

    print('\nInOrder')
    in_order(bst)

    print('\nPreOrder')
    pre_order(bst)

    print('\nPostOrder')
    post_order(bst)

