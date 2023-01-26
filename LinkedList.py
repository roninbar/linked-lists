from typing import Iterable, Iterator

import ll


class LinkedList:

    def __init__(self, xs: Iterable = ...):

        def make_list(it: Iterator):
            try:
                x = next(it)
                return x, make_list(it)
            except StopIteration:
                return ()

        self._head = make_list(iter(xs)) if xs is not ... else ()

    def __repr__(self):
        return '(' + ' '.join(map(str, self)) + ')'

    def __iter__(self):
        return LinkedListIterator(self._head)

    def __add__(self, other):

        if isinstance(other, LinkedList):
            result = LinkedList()
            result._head = ll.concat(self._head, other._head)
            return result
        else:
            raise TypeError(f'Expected a LinkedList but got {other}.')

    def __reversed__(self):
        xs = LinkedList()
        xs._head = ll.reversed(self._head)
        return xs

    def sorted(self):
        xs = LinkedList()
        xs._head = ll.sorted(self._head)
        return xs


class LinkedListIterator:

    def __init__(self, head):
        self._curr = head

    def __next__(self):
        if self._curr != ():
            x, self._curr = self._curr
            return x
        else:
            raise StopIteration


if __name__ == '__main__':
    xs = LinkedList([1, 2, 3])
    ys = LinkedList([4, 5, 6])
    print(reversed(xs + ys))
    zs = LinkedList([5, 2, 3, 4, 6, 1])
    print(zs.sorted())
