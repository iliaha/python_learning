list_result = []
while True:
    num_list = input('Введите список. Чтобы закончить введите СТОП: ').split()
    if num_list[0] == 'СТОП':
        break
    for el in num_list:
        try:
            list_result.append((int(el)))
        except ValueError:
            print(f'{el} не является числом! Недобавляю!')
    print(f'Полученный список: {list_result}')
