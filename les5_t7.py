import json
count = 0
aver_profit = 0
dict_prof = {}
list_prof = []
with open('les5_t7.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        name, form, profit, costs = line.split()
        dict_prof[name] = int(profit) - int(costs)
        if dict_prof.setdefault(name) >= 0:
            aver_profit += dict_prof.setdefault(name)
            count += 1
    if count != 0:
        aver_profit = aver_profit / count
    list_prof = {'средняя прибыль': round(aver_profit)}
    dict_prof.update(list_prof)

    print(f'Прибыль каждой компании - {dict_prof}')

with open('file_7.json', 'w') as write_js:
    json.dump(dict_prof, write_js)
