raiting_list = [8, 6, 5, 5, 3]
number = int(input("Введите число: "))
pos = 0
# нахождеие позиции
while number < raiting_list[pos]:
    pos += 1
    # если позиция конечная, то проверку останавливаем
    if pos == len(raiting_list):
        break
# проверяем находимся ли мы в конце
if pos == len(raiting_list):
    raiting_list.append(number)
# если не в конце, то проверяем есть ли введеное число в нашем рейтинге
else:
    # если введеное число есть, то приписываем его после одинаковых
    if number == raiting_list[pos]:
        raiting_list.insert(raiting_list.index(number) + raiting_list.count(number), number)
    else:
        # в ином случае записываем на свою позицию
        raiting_list.insert(pos, number)
print(f'Рейтинг с новым элементом: {raiting_list}')
