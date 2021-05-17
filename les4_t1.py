from sys import argv
scrypt_name, work_hour, cost_hour, primary = argv
try:
    salary = (float(work_hour) * float(cost_hour)) + float(primary)
    print(f'Заработная плата сотрудника: {salary:.2f}')
except ValueError:
    print(f'Значения должны быть числа!')