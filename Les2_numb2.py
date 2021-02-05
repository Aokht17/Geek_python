def cross():
    """
    The function requests the elements of the list one by one
    and produces the rearranged list
    (the order of each pair of elements is changed)
    :return: new list
    """
    my_list = []
    n = int(input('Сколько элементов ожидается в списке?'))
    for i in range (n):
        my_list.append(input('введите элемент'))
    new_list = []
    for i in range(0, n, 2):
        if i + 2 <= n:
            new_list.append(my_list[i+1])
        new_list.append(my_list[i])
    return new_list

print(cross())