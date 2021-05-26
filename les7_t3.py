class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'Число ячеек общей клетки: {self.quantity + other.quantity}'

    def __sub__(self, other):
        return f'Число ячеек общей клетки: {self.quantity - other.quantity}' if self.quantity - other.quantity > 0 else f'Нехватает клеток'

    def __mul__(self, other):
        return f'Число ячеек общей клетки: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Число ячеек общей клетки: {self.quantity // other.quantity}'

    def make_order(self, cells_in_row):
        new_row = ''
        for i in range(int(self.quantity / cells_in_row)):
            new_row += '*' * cells_in_row + '\n'
        new_row += '*' * (self.quantity % cells_in_row) + '\n'
        return new_row


Cell1 = Cell(50)
Cell2 = Cell(40)
print(Cell1 + Cell2)
print(Cell1 - Cell2)
print(Cell1 * Cell2)
print(Cell1 / Cell2)
print(Cell1.make_order(10))
print('')
print(Cell2.make_order(8))
