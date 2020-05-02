import pytest

# Design a stack with a function min that has a function min that returns the minimum value in the stack
# in O(1) time

from stack import Stack as StackBase


# Could make this more efficient by storing a ptr to the node w/ the min value if values are large

class Stack(StackBase):

    def push(self, value):
        if self.is_empty():
            super().push(value)
            self.top.min = value

        else:
            super().push(value)
            if self.top.next.min > value:
                self.top.min = value
            else:
                self.top.min = self.top.next.min


    def get_min(self):
        self._assert_not_empty()
        return self.top.min


def test_get_min():
    s = Stack()
    values = [7,5,8,4,0,9,2,]

    for v in values:
        s.push(v)

    for i in range(len(values), 0, -1):
        min_range = values[0:i]
        stack_min = s.get_min()
        assert stack_min == min(min_range)
        s.pop()

    assert s.is_empty()
