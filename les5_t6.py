with open('les5_t6.txt', 'r', encoding='UTF-8') as file:
    dict = {}
    for line in file:
        name_sub, cou_lect, cou_prac, cou_lab = line.split()
        dict[name_sub] = (int(cou_lect) if cou_lect != '-' else 0) + (int(cou_prac) if cou_prac != '-' else 0) + (int(cou_lab) if cou_lab != '-' else 0)
    print(f'Полученый словарь: {dict}')