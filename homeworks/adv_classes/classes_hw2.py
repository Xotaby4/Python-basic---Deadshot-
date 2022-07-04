from abc import ABC, abstractmethod
'''I think this task was given to us so that we would not go into game development'''
class Figure(ABC):
    def __init__(self, name, coordinate, team):
        self.name = name
        self.coordinate = coordinate
        self.team = team

    @property
    def display_name(self):
        return f'{self.name} ({self.team}) - {self.coordinate}'

    @classmethod
    def create_from_dict(cls, in_dict: dict):
        return cls(name = in_dict.get('FNAME'), coordinate = in_dict.get('FCOORDINATE'),
                   team = in_dict.get('FTEAM'))

    @abstractmethod
    def check_cell(self, new_coordinate):
        ''' Let the board have coordinates (0-7)x(0-7)'''
        if (0 <= new_coordinate[0] <= 7) and (0 <= new_coordinate[1] <= 7):
            pass
        else:
            raise Exception('Cell outside the board')
        return True


class Pawn(Figure):
    def next_step(self):
        if self.team.lower() == "white":
            self.next_step_coordinate = (self.coordinate[0], self.coordinate[1] +1)
        elif self.team.lower() == "black":
            self.next_step_coordinate = (self.coordinate[0], self.coordinate[1] - 1)
        else:
            raise Exception('Wrong team')

    def check_cell(self, new_coordinate):
        '''The pawn moves only forward'''
        super(Pawn, self).check_cell(new_coordinate=new_coordinate)
        self.next_step()
        if new_coordinate == self.next_step_coordinate:
            return True
        else:
            return False

class Horse(Figure):
    def next_step(self):
        self.possible_moves = [
            (self.coordinate[0] - 1, self.coordinate[1] - 2),
            (self.coordinate[0] - 1, self.coordinate[1] + 2),
            (self.coordinate[0] - 2, self.coordinate[1] - 1),
            (self.coordinate[0] - 2, self.coordinate[1] + 1),
            (self.coordinate[0] + 1, self.coordinate[1] - 2),
            (self.coordinate[0] + 1, self.coordinate[1] + 2),
            (self.coordinate[0] + 2, self.coordinate[1] - 1),
            (self.coordinate[0] + 2, self.coordinate[1] + 1),
        ]

    def check_cell(self, new_coordinate):
        '''The horse has up to 8 cells for the next move'''
        super(Horse, self).check_cell(new_coordinate=new_coordinate)
        self.next_step()
        if new_coordinate in self.possible_moves:
            return True
        else:
            return False

horse_dict = {'FNAME': 'Horse 1', 'FCOORDINATE': (6, 7), 'FTEAM': 'black'}
horse = Horse.create_from_dict(horse_dict)
print(horse.display_name)
#Horse 1 (black) - (2, 2)
pawn0 = Pawn ("Pawn", (0, 1), "white")
print(pawn0.check_cell((0, 2)))
#True
print(pawn0.check_cell((1, 2)))
#False
print(horse.check_cell((7, 5)))
#True
print(horse.check_cell((0, 0)))
#False