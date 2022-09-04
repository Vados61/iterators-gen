def flat_generator(my_list):
    for sub_list in my_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)
