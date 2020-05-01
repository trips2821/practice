from linked_list import LinkedList, Node


def test_create_linked_list():
    ll = LinkedList()
    assert ll.head is None


def test_append_node_no_head():
    n = Node(1)

    ll = LinkedList()
    ll.append_node(n)

    assert ll.head is n


def test_append_node_w_head():
    n1 = Node(1)
    n2 = Node(2)

    ll = LinkedList()
    ll.head = n1

    ll.append_node(n2)

    assert ll.head.next is n2


def test_append_value():
    ll = LinkedList()

    values = [1, 2,]
    for v in values:
        ll.append_value(v)

    assert ll.head.value == values[0]
    assert ll.head.next.value == values[1]


def test_find_node_by_value_head():
    ll = LinkedList()

    head_value = 1
    values = [head_value, 2, 3, 4, 5]
    for v in values:
        ll.append_value(v)

    n = ll.find_by_value(head_value)

    assert ll.head is n


def test_delete_by_node_head():
    ll = LinkedList()
    head = Node(1)

    ll.append_node(head)
    assert ll.head is head

    ll.delete_by_node(head)
    assert ll.head is None


def test_delete_by_node_not_head():
    ll = LinkedList()

    values = [1, 2, 3]
    for v in values:
        ll.append_value(v)

    node_value_to_delete = values[1]
    node_to_delete = ll.find_by_value(node_value_to_delete)

    ll.delete_by_node(node_to_delete)
    assert not ll.find_by_value(node_value_to_delete)

    ll.print()


def test_delete_by_node_last_node():
    ll = LinkedList()

    values = [1, 2, 3]
    for v in values:
        ll.append_value(v)

    node_value_to_delete = values[-1]
    node_to_delete = ll.find_by_value(node_value_to_delete)

    ll.delete_by_node(node_to_delete)
    assert not ll.find_by_value(node_value_to_delete)

    ll.print()


def test_delete_by_value():
    ll = LinkedList()

    values = [1, 2, 3]
    for v in values:
        ll.append_value(v)

    node_value_to_delete = values[-1]

    ll.delete_by_value(node_value_to_delete)
    assert not ll.find_by_value(node_value_to_delete)

    ll.print()


def test_print():
    ll = LinkedList()

    values = [1, 2, 3]
    for v in values:
        ll.append_value(v)

    print(ll)


def test_get_values():
    ll = LinkedList()

    values = [1, 2, 3]
    for v in values:
        ll.append_value(v)

    assert values == ll.get_values()
