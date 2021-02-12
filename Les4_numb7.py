def fact(n):
    """
    creates a generator with factorials of numbers from 1 to n
    :param n: positive integer
    :return: generator
    """
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        yield factorial


print(fact(6))
for numb, el in enumerate(fact(6), 1):
    print(f'{numb}! = {el}')

#def fact(n):
    #if n== 0:
        #return 1
    #return fact(n-1) * n
