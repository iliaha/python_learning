class Data:

    # def __init__(self, data_input):
    #     self.data_input = data_input

    @classmethod
    def data_num(cls, data_input):
        day, month, year = map(int, data_input.split('-'))
        print(day, month, year)

    @staticmethod
    def data_correct(data_input):
        day, month, year = map(int, data_input.split('-'))
        if 0 != day <= 31:
            if 0 < month <= 12:
                if -2100 <= year <= 2100:
                    print("Дата существует")
                else:
                    print('Такого года не существует')
            else:
                print('Такого месяца не существует')
        else:
            print('Такого дня не существует')


data1 = Data()
data1.data_num('12-12-2012')
data1.data_correct('12-12-2012')
