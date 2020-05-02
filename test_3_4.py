import pytest

# Implement a Queue using 2 stacks

from stack import Stack as StackBase


# Worst case scenario each add and remove takes O(n)

class StackQueue(StackBase):
    reversed = False

    def add(self, value):
        if self.reversed:
            self._flip()

        self.push(value)

    def remove(self):
        if not self.reversed:
            self._flip()

        return self.pop()

    def _flip(self):
        self.reversed = not self.reversed

        s = StackBase()
        while not self.is_empty():
            value = self.pop()
            s.push(value)

        self.top = s.top


def test_stack():
    sq = StackQueue()
    values = [1,2,3,4,5,6,7,8,9]

    for v in values:
        sq.add(v)

    for v in values:
        assert sq.remove() == v
