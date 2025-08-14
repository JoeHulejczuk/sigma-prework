integers = [2, 4, 1, 0, 2, -1]


def maxmin(list):
    list.sort()
    maxi = list[-1]
    mini = list[0]
    return [mini, maxi]


print(f'The min and max of the list are: {maxmin(integers)}')
