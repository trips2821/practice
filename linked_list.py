
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        ptr = self.head
        while ptr is not None:
            values.append(str(ptr.value))
            ptr = ptr.next

        values_string = "\n".join(values)
        return values_string

    def append_value(self, value):
        n = Node(value)
        self.append_node(n)

    def append_node(self, node):
        if self.head is None:
            self.head = node
        else:
            ptr = self._get_last_node()
            ptr.next = node

    def _get_last_node(self):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        return ptr

    def find_by_value(self, value):
        ptr = self.head
        return self._find_next(ptr, value)

    def _find_next(self, ptr, value):
        while ptr is not None:
            if ptr.value == value:
                return ptr
            else:
                ptr = ptr.next
        return False

    def delete_by_node(self, node):
        last_node = None
        ptr = self.head
        while ptr is not None:
            if ptr is node:
                next_node = node.next
                if last_node is not None:
                    last_node.next = next_node
                else:
                    self.head = next_node
                return True
            else:
                last_node = ptr
                ptr = ptr.next

    def delete_by_value(self, value):
        node = self.find_by_value(value)
        if node:
            self.delete_by_node(node)
            return True
        else:
            return False

    def print(self):
        print()
        ptr = self.head
        while ptr is not None:
            print(ptr.value)
            ptr = ptr.next

    def get_values(self):
        ptr = self.head

        values = []
        while ptr is not None:
            values.append(ptr.value)
            ptr = ptr.next

        return values
