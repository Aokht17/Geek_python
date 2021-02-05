month = int(input('Введите номер месяца'))
# изящнее было бы сделать словарь наоборот
season_dict = {1: 'winter', 2: 'winter', 3: 'spring',
               4: 'spring', 5: 'spring', 6: 'summer',
               7: 'summer', 8: 'summer', 9: 'autumn',
               10: 'autumn', 11: 'autumn', 12: 'winter'}
season_list = ['winter', 'spring', 'summer', 'autumn', 'winter']
print(season_dict[month])
print(season_list[month // 3])
