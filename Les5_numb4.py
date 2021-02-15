with open('numbers.txt', 'r') as inp_file, open('rus_num.txt', 'w') as out_file:
    rus_numbers = ['Один', 'Два', 'Три', 'Четыре']
    i = 0
    for line in inp_file:
        if line.strip():
            out_file.write(rus_numbers[i] + ' - ' + line.split(' ')[2])
            i += 1
