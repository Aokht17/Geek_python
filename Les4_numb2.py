def compare_previous(my_list):
    """
    creates new list with elements of the original list,
    the values of which are greater than the previous element
    :param my_list: list of integer
    :return: new lust from generator
    """
    return [my_list[i] for i in range(1, len(my_list))
            if my_list[i] > my_list[i - 1]]


print(compare_previous([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))
