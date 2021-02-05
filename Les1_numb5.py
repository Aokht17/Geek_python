gain = float(input("Введите значение выручки"))
loss = float(input("Введите значение издержек"))
if gain > loss:
    print("Фирма работает с прибылью")
    print("Рентабельность составляет {:.2f}%".format((gain - loss) / gain * 100))
    hum = int(input("Введите количество сотрудников"))
    print("Прибыль фирмы в расчете на одного сотрудника: {:.2f}".format((gain - loss) / hum))
elif gain < loss:
    print("Фирма работает с убытком, упс")
else:
    print("Фирма выходит в ноль")
