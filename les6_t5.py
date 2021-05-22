class Stationery:
    title = 'Канцелярская принадлежность'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Отрисовка {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Отрисовка {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Отрисовка {self.title}')


pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
