with open('les5_t3.txt', 'r') as file:
    list_bad = []
    list_sal = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            list_bad.append(i[0])
        list_sal.append(i[1])
    print(f"Сотрудники с окладом меньше 20000 р.: {', '.join(list_bad)}")
    print(f'Средняя величина дохода: {sum(map(int, list_sal)) / len(list_sal)} руб.')
