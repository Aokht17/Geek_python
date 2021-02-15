def write_and_sum(file_name):
    """
    creates new file, adds your numbers(integers) and summarizes them
    :param file_name: the name of file to be created
    :return: sum of integers from input
    """
    with open(file_name, 'w+') as file:
        while True:
            new_str = input('Ввод. Для прекращения ввода введите пустую строку')
            file.write(new_str + ' ')
            if not new_str:
                break
        # Это просто для ввода от пользователя. В таком случае удобно
        # сразу подсчитывать сумму при вводе, но я все же сделаю
        # через считывание из файла
        file.seek(0)
        f = file.readlines()[0].strip()
        return sum([int(i) for i in f.split()])


print(write_and_sum('created_num_file.txt'))
