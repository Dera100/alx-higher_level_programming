#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Check for divisibility by 2 code

    Args:
        my_list: the list of int code

    Returns:
        return the bool value of result area
    """
    new_list = []
    for i in my_list:
        new_list.append(i % 2 == 0)
    return (new_list)
