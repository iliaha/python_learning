from math import factorial
from itertools import count

def fact():
    for el in count(1):
        yield factorial(el)

num = int(input('Введите число факториалов: '))
x = 1
for el in fact():
    print(f'{x}! = {el}')
    x += 1
    if x > num:
        break
