with open('les5_t2.txt', 'r') as file:
    cou_lin = file.read().split('\n')
    print(f'Кол-во строк в файле: {len(cou_lin)}')
    for num, i in enumerate(cou_lin):
        word = i.split()
        print(f'Кол-во слов в {num + 1} строке: {len(word)}')
