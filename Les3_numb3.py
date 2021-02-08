def my_func(arg_1, arg_2, arg_3):
    """
    the function takes three positional arguments,
    and returns the sum of the largest two arguments
    """
    return sum(sorted([arg_1,arg_2,arg_3], reverse=True)[0:2])


print(my_func(10, 4, 7))