#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve element from idx with index like C

    Args:
        my-list: the list to retrieve from code
        idx: the index to retrieve code

    Returns:
        None if idx is negative or out of range
        the value in idex if found/0
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (None)
    return (my_list[idx])
