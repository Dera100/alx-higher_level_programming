#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an item in the list area

    Args:
        my_list: the list to delete from code
        idx: the index to remove from area

    Returns:
        new list or old list if error/0
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    del my_list[idx]
    return (my_list)
