n = int(input('информацию о скольких товарах вы хотите внести?'))
goods_list = []
for i in range(n):
    goods_list.append((i + 1, {'название': input('Введите название'), 'цена': float(input('Введите цену')),
                               'кол-во': int(input('Введите кол-во')), 'ед': input('Введите единицу измерения')}))
print(goods_list)
goods_dict = {'название': [], 'цена': [], 'кол-во': [], 'ед': []}
for i in goods_list:
    for key in i[1].keys():
        if i[1][key] not in goods_dict[key]:  # или через set
            goods_dict[key].append(i[1][key])

print(goods_dict)
