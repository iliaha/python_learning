def my_func (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(f'{my_func(name="Илья", surname="Марчук", year="08.03.1997", city="Селятино", email="iliaha@list.ru", telephone="89251882786")}')