import pytest


from minimal_bst import create_minimal_bst

# Given and ordered array, write a func that generates a binary search tree of minimal height

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
    values = range(17)

    bst = create_minimal_bst(values, 0, len(values) - 1)

    print('\nInOrder')
    in_order(bst)

    print('\nPreOrder')
    pre_order(bst)

    print('\nPostOrder')
    post_order(bst)

