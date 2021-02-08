def division():
    """
    divides numbers (int, float)
    :return: the quotient and remainder (float)
    """
    dividend = float(input('Введите делимое'))
    divisor = float(input('Введите делитель'))
    try:
        quo, rem = divmod(dividend, divisor)
        print(f'Частное {quo}, остаток {rem}')
    except ZeroDivisionError:
        print('На ноль не делим')
        division()

division()