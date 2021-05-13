def int_func(words):
    list = []
    for i in range(len(words)):
        list.append(words[i].title())
    return ' '.join(list)
print(int_func(input("Введите слова: ").split()))

# def int_func_list(*args):
#     list = input('Введите слова: ')
#     print(list.title())
#     return
# int_func_list()
