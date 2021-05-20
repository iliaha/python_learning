with open('les5_t1.txt', 'w+') as f:
    ex = True
    while ex == True:
        line = (input('Введите строку. Для выхода нажмите Enter: '))
        if line == '':
            ex = False
            break
        f.write(line + '\n')
    f.seek(0)
    for el in f:
        print(el)
