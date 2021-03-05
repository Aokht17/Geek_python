class OwnError(Exception):
    def __init__(self, message):
        self.message = message


a = input('Введите делимое ')
b = input('Введите делитель ')
try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise OwnError("Division by zero is not allowed")
except ValueError:
    print('not number type')
except OwnError as ex:
    print(ex)
else:
    print(a / b)
