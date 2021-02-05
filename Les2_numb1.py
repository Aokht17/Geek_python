my_list = []
my_list.append([True, 'spring', 45.8])
my_list.extend([True, 'spring', 45.8, 90])
my_list.insert(3, (5, ['abs'], False))
for i in my_list:
    print(type(i))

print(my_list)