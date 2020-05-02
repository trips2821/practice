
class StackEmptyException(Exception):
    pass


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        self._assert_not_empty()

        return_value = self.top.value
        self.top = self.top.next

        return return_value

    def peek(self):
        self._assert_not_empty()

        return self.top.value

    def _assert_not_empty(self):
        if self.is_empty():
            raise StackEmptyException
