def flat_generator_enhanced(my_list):
    for elem in my_list:
        if isinstance(elem, list):
            for sub_elem in flat_generator_enhanced(elem):
                yield sub_elem
        else:
            yield elem


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', ['e', '45', ['r', 34], ['r', 34]], 'f', 'h', False],
        [1, 2, None],
    ]
    for item in flat_generator_enhanced(nested_list):
        print(item)