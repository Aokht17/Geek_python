total_time = int(input('Enter time in secs'))
# можно было не плодить столько переменных,
# но так просто удобнее показать все методы форматирования строк
hs = total_time / 3600
mins = total_time % 3600 / 60
sec = total_time % 360 % 60
print("Your time is %d:%d:%d" % (hs, mins, sec))
print("Your time is {:.0f}:{:.0f}:{}".format(hs, mins, sec))
print(f"Your time is {int(hs)}:{int(mins)}:{sec}")
