user_number = input('Enter positive integer number')
# первый вариант - чуть менее костыльный
n = 0
max_num = 0
while n < len(user_number):
    if int(user_number[n]) > max_num:
        max_num = int(user_number[n])
    n += 1
print(max_num)

# другой вариант (возможно я перемудрила)
user_number = int(user_number)
max_num1 = 0
m = 10
while True:
    if user_number % m // (m // 10) > max_num1:
        max_num1 = user_number % m // (m // 10)
    if user_number // m < 1:
        break
    user_number -= user_number % m
    m *= 10
print(max_num1)
