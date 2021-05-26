from abc import ABC, abstractmethod


class Clothes(ABC):
    all_square_num = 0

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def square(self):
        pass

    @property
    def all_square(self):
        return self.all_square_num


class Coat(Clothes):

    @property
    def square(self):
        Clothes.all_square_num += (self.param / 6.5 + 0.5)
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def square(self):
        Clothes.all_square_num += (2 * self.param + 0.3)
        return 2 * self.param + 0.3


black_coat = Coat(10)
red_coat = Coat(20)
blue_suit = Suit(15)
green_suit = Suit(25)

print(black_coat.square)
print(red_coat.square)
print(blue_suit.square)
print(green_suit.square)
print(black_coat.all_square)
