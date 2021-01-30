a = float(input("Сколько километров пробежал спортсмен в 1 день?"))
b = float(input("Сколько должен пробежать спортсмен?"))
day = 1
while True:
    if a >= b:
        break
    a *= 1.1
    day += 1
print(day)
