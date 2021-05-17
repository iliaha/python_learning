from sys import argv
from itertools import count

my_list = []
file_name, start_num = argv
for el in count(int(start_num)):
    if el > 20:
        break
    else:
        my_list.append(el)
print(f'Сгенерированые числа: {my_list}')