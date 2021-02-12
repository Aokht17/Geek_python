def unique_el(my_list):
    """
    creates new list with unique items of a given list
    :return: new list
    """
    return [i for i in my_list if my_list.count(i) == 1]


print(unique_el([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]))
