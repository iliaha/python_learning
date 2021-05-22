class Worker:

    name = None
    surname = None
    position = None  # Должность
    _income = {}  # Доход

    def __init__(self, name_per, surname, position, wage, bonus):
        self.name_per = name_per
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name_per, surname, position, wage, bonus):
        super().__init__(name_per, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.surname} {self.name_per}')

    def get_total_income(self):
        print(f"Доход с учетом премии: {self._income.get('wage') + self._income.get('bonus')}")


name = Position('Илья', 'Марчук', 'грузчик', 40000, 15000)
name.get_full_name()
name.get_total_income()
