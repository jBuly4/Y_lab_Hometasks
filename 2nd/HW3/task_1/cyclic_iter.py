from itertools import cycle


class CyclicIterator:
    def __init__(self, iterable):
        self.iterator = cycle(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
