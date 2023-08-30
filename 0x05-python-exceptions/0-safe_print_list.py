#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print the elements in the list

    Args:
        my_list (list): the list containing the data
        x (int): integer for date in the list

    Returns:
        The number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end=' ')
            count += 1
        except IndexError:
            break
    print()
    return count
  