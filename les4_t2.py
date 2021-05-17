task_list = [37, 125, 88, 1, 1, 87, 23, 12, 11]
new_list = [el for el in task_list if el > task_list[task_list.index(el) - 1]]
print(f'Исходный список: {task_list}')
print(f'Новый список: {new_list}')