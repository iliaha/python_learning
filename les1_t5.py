revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if costs > revenue:
    print("Фирма работает в убыток! =(")
else:
    print("Фирма приносит прибыль! =)")
    profit = revenue - costs # Считаем прибыль
    profitability = profit / revenue # Считаем рентабельность
    num_staff = int(input("Введите кол-во сотрудников: "))
    profit_staf = profit / num_staff # Считаем прибыль на сотрудника
    print(f"Прибыль: {profit}, рентабельность выручки: {profitability:.2f}, прибыль на одного сотрудника: {profit_staf:.2f}")