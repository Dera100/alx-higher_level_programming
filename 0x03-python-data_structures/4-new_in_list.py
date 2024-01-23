#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replace element in list without modifying the org list area

    Args:
        my_list: the list code
        idx: the index code
        element: the element to modify code

    Returns:
        new_list or org_list if idx < 0 or
        out of range code
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list.copy())
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
