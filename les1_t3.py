n = input("Введите число: ")
number = n ## Число которое будем складывать
i = 1  ## Счётчик
total = 0 ## Сумма
while i <= int(n):
    total = total + int(number)
    if i == int(n): ## Проверка приписывать ли к числу на сложение дополнительный символ
        break
    else:
        number = number + n
        i = i + 1
print(f'Сумма: {total}')