num_month = int(input("Введите номер месяца: "))
list_month = ["зима", "весна", "лето", "осень"]
dict_mounth = {0 : "зима", 1 : "весна", 2 : "лето", 3 : "осень"}
while num_month < 1 or num_month > 12:
    print("Такого месяца не существует!")
    num_month = int(input("Введите номер месяца: "))
if num_month == 12 or num_month == 1 or num_month == 2:
    n = 0
elif num_month == 3 or num_month == 4 or num_month == 5:
    n = 1
elif num_month == 6 or num_month == 7 or num_month == 8:
    n = 2
elif num_month == 9 or num_month == 10 or num_month == 11:
    n = 3
print(f"Введенный месяц: {list_month[n]}, {dict_mounth.get(n)}")
