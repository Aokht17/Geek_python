with open('created_file.txt', 'r+') as file:
    for line in file:  # посмотрим что уже есть в файле
        print(line)
    print('new string', file=file)  # добавим еще одну строчку
    str_list = ['add1\n', 'add2\n']  # и еще парочку
    file.writelines(str_list)
    file.seek(0)  # вернемся в начало
    not_blank = 0
    for line in file:
        if line.strip():  # посчитаем только непустые строки
            not_blank += 1
            print(f'В {not_blank} строке {len(line.split())} слов(a)')
    print(f'Всего {not_blank} непустых строк')
