def sum_func():
    sum = 0
    ex = True
    while ex == True:
        num = input('Введите числа через пробел или Q для выхода: ').split()
        for i in range(len(num)):
            if num[i] == 'q' or num[i] == 'Q':
                ex = False
                break
            else:
                sum += int(num[i])
        print(f'Сумма введенных чисел: {sum}')
sum_func()
