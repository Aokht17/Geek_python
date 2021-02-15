from statistics import mean
import json

with open('firma.txt', 'r') as file:
    profit_dict = {}
    for line in file:
        if line.strip():
            profit = int(line.split()[2]) - int(line.split()[3])
            profit_dict.update({line.split()[0]: profit})
    print(profit_dict)
    average_profit = mean([i for i in profit_dict.values() if i >= 0])
    print(f'Средняя прибыль составляет {average_profit}')

profit_list = [profit_dict, {'average_profit': average_profit}]
print(profit_list)

with open('firma.json', 'w') as output:
    json.dump(profit_list, output)
