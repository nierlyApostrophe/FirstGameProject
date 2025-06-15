from abc import ABC

class Unit(ABC):

    name: str = "UN"
    symbol: str = "u"

    def __init__(self):
        self.moves: int = 0
        self.health: int = 0
        self.damage: int = 0
        self.x: int = 0
        self.y: int = 0

    def move(self, delta_x: int, delta_y: int, board_size: int) -> None:
        """
        Allows to move the unit over the set amount of moves or less

        :param delta_x: vertical change
        :param delta_y: horizontal change
        :param board_size: the size of your board
        """
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        distance = abs(delta_x) + abs(delta_y)

        if 0 <= new_x < board_size and 0 <= new_y < board_size:
            if distance <= self.moves:
                self.x = new_x
                self.y = new_y
                print(f"You've moved your {self.name} {distance} squares to {self.x, self.y}")
            else:
                print("The square is too far, this unit cannot reach it.")
        else:
            print("Invalid move. You've reached the end of the board.")

    def is_dead(self) -> bool | None:
        """
        Removes the unit from the board whenever its health fully depletes
        """
        if self.health <= 0:
            return True

class Infantry(Unit):

    name = "infantry"
    symbol = "in"

    def __init__(self):
        super().__init__()
        self.moves = 2
        self.health = 4
        self.damage = 4


class Cavalry(Unit):

    name = "cavalry"
    symbol = "cv"

    def __init__(self):
        super().__init__()
        self.moves = 4
        self.health = 10
        self.damage = 1

if __name__ == "__main__":
    help(Unit)
    help(Infantry)
    help(Cavalry)
