# я не поняла, можно ли использовать NumPy, но наверно нет

class Matrix:
    def __init__(self, matrix):
        the_len = len(next(iter(matrix)))
        if all(len(l) == the_len for l in matrix):
            self.matrix = list(matrix)
        else:
            raise ValueError('not all rows have same length!')

    def __str__(self):
        y = "\n".join(str(self.matrix).replace('[', '').replace(',', '').split(']'))
        return f' {y}'

    def __next__(self):
        self.index = 0
        if self.index < len(self.matrix):
            self.index += 1
            return self.matrix[self.index-1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            sum_list = []
            for item1, item2 in zip(self.matrix, other.matrix):
                sum_list.append([i + j for i, j in zip(item1, item2)])
            return Matrix(sum_list)
        else:
            return 'Matrices should have similar dimensions!'

my_matrix = Matrix([[1, 2], [3, 455], [5, 6], [7, 8]])
matrix_2 = Matrix([[8, 2], [3, 4], [7, 6], [9, 4]])
print(my_matrix)
print(matrix_2)
print(my_matrix + matrix_2)
