def func_with_oper(x, y):
    return 1 / x ** abs(y)

def func_without_oper(x, y):
    for i in range(abs(y)-1):
        x *= x
    return 1 / x
x = float(input("Введите число: "))
y = int(input("Введите отрицательную степень числа: "))

print(f'Результат (со встроеной функцией): {func_with_oper(x, y):.4f} Результат (без встроенной функцией): {func_without_oper(x, y):.4f}')