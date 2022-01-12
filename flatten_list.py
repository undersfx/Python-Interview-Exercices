'''
    Given a lists with nested lists, create a function that returns
    a flat list with values at the same order.

    e.g. Given [[1], 2, [3, [4, 5]]], return [1, 2, 3, 4, 5]
'''

def flatten(input_list):
    """ Flatten a list with nested lists

        Time:   O(n) (n = input_list)
        Memory: O(m) (m = biggest nested list)
    """
    flat = []

    def wrapper(input_list):
        for item in input_list:
            if isinstance(item, list):
                wrapper(item)
            else:
                flat.append(item)
        return flat

    return wrapper(input_list)


nested = [[1], 2, [3, [4, 5, 6]], [7, 8], [9, [10]]]
print(f'{nested} => {flatten(nested)}')