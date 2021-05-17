from functools import reduce

task_list = [el for el in range(99, 1001) if el % 2 == 0]
print(f'Произведение всех чисел: {reduce(lambda num1, num2: num1 * num2, task_list)}')
