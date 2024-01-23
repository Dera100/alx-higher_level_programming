#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add two tuple and returna tuple ares

    Args:
        tuple_a: the first tuple area
        tuple_b: the second tuple area

    Returns:
        the resulr of sum of two first  elment of
        each tuple area
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
