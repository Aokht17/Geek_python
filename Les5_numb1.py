with open('created_file.txt', 'w') as new_file:
    while True:
        new_str = input('Ввод')
        new_file.write(new_str + '\n')
        if not new_str:
            break

