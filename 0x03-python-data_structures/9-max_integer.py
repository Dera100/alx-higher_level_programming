#!/usr/bin/python3
def max_integer(my_list=[]):
    """find the max element in list area

    Args:
        my_list: the list that contains the int area

    Returns:
        return the max element/0
    """
    if len(my_list) == 0:
        return (None)
    min_value = -10000000
    for i in my_list:
        if i > min_value:
            min_value = i
    return (min_value)
