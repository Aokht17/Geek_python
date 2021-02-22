class Cell:
    def __init__(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            print('Number of cells can be only integer!')

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell(self.number - other.number) if self.number - other.number > 0 else print(
            'The difference must be positive')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))

    def make_order(self, num_in_row):
        if self.number // num_in_row >=1:
            n = ('*' * num_in_row + ',') * (self.number // num_in_row) + '*' * (self.number % num_in_row)
            return "\n".join(str(n).split(','))
        else:
            return 'impossible to use this row number'


a = Cell(12)
b = Cell(5)
print(a + b, (a + b).number)
print((a / b).number)
print(a.make_order(5))
