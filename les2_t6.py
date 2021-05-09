count_product = int(input("Введите кол-во товара: "))
num = 1
task_tuple = []   # Список кортежей
anality_dict = {"название": [], "цена": [], "колличество": [], "eд": []}  # Словарь для анализа
while num <= count_product:
    # Словарь для кортежа пересоздаем каждый раз, для того чтоб пропала ссылка разных пар кортежей на один словарь
    tul_dict = {"название": "", "цена": "", "колличество": "", "eд": ""}
    for key in tul_dict.keys():  # Заполнение словаря для кортежа
        tul_dict[key] = int(input(f'Введите {key}: ')) if (key == "цена" or key == "колличество") else input(f'Введите {key}: ')
        anality_dict[key].append(tul_dict[key])  # Запись значений в словарь для анализа
    task_tuple.append((num, tul_dict))  # Запись в список кортежа
    num += 1
print("Сводная таблица")
for value in task_tuple:
    print(f"{value}")
print("Таблица для анализа")
for key, value in anality_dict.items():
    print(f"{key} {value}")
