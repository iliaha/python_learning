def my_func(arg1, arg2, arg3):
    sum = 0
    max1 = arg1
    max2 = arg2
    if arg3 > max2:
        max2 = arg3
    if arg3 > max1:
        max1 = arg3
    sum = max1 + max2
    return sum

arg1 = float(input("Введите первое число: "))
arg2 = float(input("Введите второе число: "))
arg3 = float(input("Введите третье число: "))
res = my_func(arg1, arg2, arg3)
print(f"Результат работы: {res}")