class Road:

    _lenght_road = None
    _width_road = None

    def __init__(self, lenght, width):
        self._lenght_road = int(lenght)
        self._width_road = int(width)

    def mass(self):
        self.weight = 25
        self.thickness = 5
        print(f'Масса необходимого асфальта: {self._lenght_road * self._width_road * self.weight * self.thickness / 1000} тонн')


road = Road(20, 5000)
road.mass()
