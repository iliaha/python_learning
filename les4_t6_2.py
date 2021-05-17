from sys import argv
from itertools import cycle

my_list = ['Hello', 123, 'World', '!']
file_name, count_rep = argv
rep = 0
for el in cycle(my_list):
    if rep > int(count_rep):
        break
    rep += 1
    print(el)
