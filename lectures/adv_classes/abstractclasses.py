from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, coordinate):
        self.coordinate = coordinate

    @abstractmethod
    def move(self):
        print("Go")

    @classmethod
    @abstractmethod
    def clssss(cls):
        print("G")

    def get_coordinate(self):
        return self.coordinate


class Pawn(Figure):
    def move(self):
        super(Pawn, self).move()
        pass

    def trans_to(self, type_figure):
        pass

    @classmethod
    def clssss(cls):
        pass


Figure.clssss()
