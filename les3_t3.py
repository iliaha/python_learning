def my_func(arg1, arg2, arg3):
    list = [arg1, arg2, arg3]
    list.remove(min(arg1, arg2, arg3))
    return sum(list)

print(f'Результат работы: {my_func(float(input("Введите первое число: ")), float(input("Введите второе число: ")), float(input("Введите третье число: ")))}')