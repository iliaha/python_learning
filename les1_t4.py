numbers = int(input("Введите число: "))
max = numbers % 10
while numbers >= 1:
    if max == 9: # Если цифра из числа равна 9, то дальнейшее выполнение программы бессмыслено
        break
    numbers = numbers // 10
    if numbers % 10 > max:
        max = numbers % 10
print(f"Максимальная цифра: {max}")