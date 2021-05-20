name_file = 'les5_t5.txt'
with open(name_file, 'w+') as file:
    file.write(input('Введите числа через пробел: '))

with open(name_file, 'r') as file:
#     num_list = file.read().split()
#     res = sum(map(int, num_list))
#     print(f'Сумма числе в файле {file.name}: {res}')

#   Решение в одну строчку
    print(f'Сумма числе в файле {file.name}: {sum(map(int, file.read().split()))}')