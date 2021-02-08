def str_sum():
    """
    prompts the user for a space-separated string of numbers
    and prints the sum of the numbers. To complete the entry and summation,
    you must enter a non-numeric value (str, bool)
    :return: sum value (float)
    """
    sum_str = 0
    flag = True
    while flag:
        my_list = input('Ввод. Для окончания ввода введите любую букву').strip().split(' ')
        # strip() against breaking due to extra spaces
        for i in my_list:
            try:
                sum_str += float(i)
            except ValueError:
                flag = False
        print(f'Сумма: {sum_str}')


str_sum()