class Matrix():

    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, el)) for el in self.matrix_data])

    def __add__(self, other):
        mat_sum = []
        for el in zip(self.matrix_data, other.matrix_data):
            mat_sum.append([sum([i, j]) for i, j in zip(*el)])

        return Matrix(mat_sum)

Mat1 = Matrix([[1, 2, 3], [3, 4, 6], [5, 6, 3]])
Mat2 = Matrix([[5, 8, 55], [44, 1, 26], [57, 7, 8]])
print(Mat1, '\n')
print(Mat2, '\n')
print(Mat1 + Mat2)
