'''
Implement an interleaving Flattener, an iterator object that is itself made up
of iterator objects, giving that class a next() method that prints in an
interleaving order and a has_next() method to determine when it is done.
E.G.
arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9]
a = iter(arr1)
b = iter(arr2)
c = iter(arr3)
IterFlat = Interleaving_Flattener([a, b, c])
while IterFlat.has_next():
    print(IterFlat.next())
Should print 1, 4, 6, 2, 5, 7, 3, 8, 9
'''

import collections

class Interleaving_Flattener(object):
    def __init__(self, iterables):
        self.iterables = collections.deque(iterables)

    def _has_next(self, iterator):
        values = []
        while True:
            try:
                values.append(iterator.__next__())
            except StopIteration:
                if len(values) == 0:
                    return [iter([]), False]
                else:
                    return [iter(values), True]

    def next(self):
        if not self.has_next():
            raise StopIteration
        current = self.iterables.popleft()
        result = current.__next__()
        current, iter_left = self._has_next(current)
        if iter_left:
            self.iterables.append(current)
        return result

    def has_next(self):
        return len(self.iterables) != 0


if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    arr3 = [6, 7, 8, 9]
    a = iter(arr1)
    b = iter(arr2)
    c = iter(arr3)
    IterFlat = Interleaving_Flattener([a, b, c])
    test = []
    while IterFlat.has_next():
        test.append(IterFlat.next())
    if test == [1, 4, 6, 2, 5, 7, 3, 8, 9]:
        print('Test Passed')
