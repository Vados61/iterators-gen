class FlatIterator:

    def __init__(self, nes_list):
        self.nes_list = iter(nes_list)

    def __iter__(self):
        self.iter_list = next(self.nes_list)
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor >= len(self.iter_list):
            self.iter_list = next(self.nes_list)
            self.cursor = 0
        self.cursor += 1
        return self.iter_list[self.cursor - 1]


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
