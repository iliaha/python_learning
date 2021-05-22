from time import sleep


class TrafficLight:

    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        count = 0
        while count < 3:
            print(f'{self.__color[count]}')
            if count == 0:
                sleep(7)
            elif count == 1:
                sleep(2)
            elif count == 2:
                sleep(10)
            count += 1


Change_Light = TrafficLight()
Change_Light.running()
