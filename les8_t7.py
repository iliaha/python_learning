class Complex_number:
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def __str__(self):
        if self.b > 0:
            return f'z = {self.a} + {self.b} * i'
        else:
            return f'z = {self.a} - {abs(self.b)} * i'

    def __add__(self, other):
        if self.b + other.b > 0:
            return f'z = {self.a + other.a} + {self.b + other.b} * i'
        else:
            return f'z = {self.a + other.a} - {abs(self.b + other.b)} * i'


    def __mul__(self, other):
        if self.a * other.b + other.a * self.b > 0:
            return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b + other.a * self.b} * i'
        else:
            return f'z = {self.a * other.a - (self.b * other.b)} - {abs(self.a * other.b + other.a * self.b)} * i'


num_1 = Complex_number(1, -1)
num_2 = Complex_number(3, 6)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)
