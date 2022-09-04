class FlatIterator:

    def __init__(self, nes_list):
        self.iter_list = iter(nes_list)
        self.queue = []

    def __iter__(self):
        self.next_iteration = next(self.iter_list)
        return self

    def __next__(self):
        if not self.next_iteration:
            self.next_iteration = next(self.iter_list)
        if self.queue:
            self.next_element = self.queue.pop(0)
        else:
            self.next_element = self.next_iteration.pop(0)
        while isinstance(self.next_element, list):
            self.queue = self.next_element + self.queue
            self.next_element = self.queue.pop(0)
        return self.next_element


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', ['e', '45', ['r', 34], ['r', 34]], 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)

    # flat_list = [item for item in FlatIterator(nested_list)]
    # print(flat_list)
