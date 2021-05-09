user_list = input("Введите слова: ")
result_list = user_list.split()
for num, el in enumerate(result_list):
    print(f'Номер слова {el [0:10]}: {num}.')
