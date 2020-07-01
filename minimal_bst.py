
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_minimal_bst(values, start_index, end_index):
    mid_index = (start_index + end_index ) // 2

    node_value = values[mid_index]
    node = Node(node_value)

    if end_index < start_index:
        return None

    node.left = create_minimal_bst(values, start_index, mid_index - 1)
    node.right = create_minimal_bst(values, mid_index + 1, end_index)

    return node
