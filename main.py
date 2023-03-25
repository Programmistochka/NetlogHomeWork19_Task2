import types


def flat_generator(list_of_lists):
    whole_list = []
    for list in list_of_lists:
        whole_list += list
    finish = len(whole_list)
    n = 0
    while n < finish:
        yield whole_list[n]
        n += 1
    
def test_2(list_of_lists):

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists), types.GeneratorType)


if __name__ == '__main__':
    
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    for item in flat_generator(list_of_lists_1):
        print(item)

    test_2(list_of_lists_1)