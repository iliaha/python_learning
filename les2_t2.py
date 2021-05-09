list_user = list(input("Введите список: "))
index = 0
print(f"Строка пользователя до изменения: {list_user}")
while index < (len(list_user) - 1): # Проверяем вхождение индекса в длину строки
    list_user[index], list_user[index + 1] = list_user[index + 1],  list_user[index]
    index += 2 # Перескакиваем через один индекс
print(f"Строка пользователя после изменения: {list_user}")
