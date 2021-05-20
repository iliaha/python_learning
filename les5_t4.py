dict = {'One': 'Раз', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_line = []
with open('les5_t4.txt', 'r', encoding='UTF-8') as file_old:
    old_line = file_old.read().split('\n')
    for i in old_line:
        i = i.split()
        new_line.append(dict[i[0]] + ' ' + i[1] + ' ' + i[2] + '\n')
#    print(new_line) делал проверку правильности списка до записи

with open('les5_t4_new.txt', 'x', encoding='UTF-8') as file_new:
    file_new.writelines(new_line)
