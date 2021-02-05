phrase = []
phrase.extend(input('Введите строку').split(" "))
for i in range(len(phrase)):
    print(i + 1, phrase[i]) if len(phrase[i]) <= 10 else print(i+1, phrase[i][:10])
