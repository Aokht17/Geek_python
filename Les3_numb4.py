def my_func(x, y):
    """
    function raises x to the power of y using **
    :param x: real positive number
    :param y: negative integer
    """
    return x ** y if x > 0 and y <= 0 else print('check the conditions')


def my_func_1(x, y):
    """
    function raises x to the power of y via cycle
    :param x: real positive number
    :param y: negative integer
    """
    if x > 0 and y <= 0:
        ans = 1
        for _ in range(abs(y)):
            ans = ans / x
        return ans
    else:
        print('check the conditions')


print(my_func(5, -3))
print(my_func_1(5, -2))
