class Car:

    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}!')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'Машина {self.name} едет со скоростью {self.speed}')
        else:
            print(f'Машина {self.name} привысила скорость на {self.speed - 60}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            print(f'Машина {self.name} едет со скоростью {self.speed}')
        else:
            print(f'Машина {self.name} привысила скорость на {self.speed - 40}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


Kia = TownCar(70, 'синяя', 'KIA Ceed SW', False)
Kia.go()
Kia.stop()
Kia.turn('направо')
Kia.show_speed()

print('-' * 50)

ferrari = SportCar(70, 'синяя', 'Ferarri F450', False)
ferrari.go()
ferrari.stop()
ferrari.turn('направо')
ferrari.show_speed()

print('-' * 50)

MAN = WorkCar(50, 'желтый', 'MAN 2121', False)
MAN.go()
MAN.stop()
MAN.turn('налево')
MAN.show_speed()
