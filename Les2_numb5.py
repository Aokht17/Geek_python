def rating(my_list):
    """
    Adds a new item to the list and sorts in descending order
    :param my_list: list of integer
    :return: sorted list
    """
    my_list.append(int(input('Введите число')))
    return sorted(my_list, reverse=True)


my_list_1 = [7, 6, 3, 1]
print(rating(my_list_1))
