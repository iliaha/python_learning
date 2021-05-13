def my_func(arg1, arg2):
   res = arg1 / arg2
   print(f"Результат деления: {res:.2f}")

arg1 = float(input('Введите делимое: '))
arg2 = float(input('Введите делитель: '))
while arg2 == 0:
    print("На ноль делить нельзя!")
    arg2 = float(input('Введите делитель: '))
my_func(arg1, arg2)
