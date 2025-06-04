import team_create as tc

class Board:
    """
    Fully defines board. Contains objects of type tc.Team in itself
    """

    max_board_size: int = 10
    min_board_size: int = 3
    _team_cap: int = 2
    _team_count: int = 0

    def __init__(self, board_size: int=min_board_size):
        if self.min_board_size <= board_size <= self.max_board_size:
            self.board_size: int = board_size # N x N matrix
        else:
            raise ValueError("Board size must be a set from 3 to 10")
        self.__board: list[list[str]] = []
        self.__occupancy_board: list[list[str]] = []
        self.empty_board()

    def empty_board(self) -> list:
        """
        Clears the board
        x - vertical, increasing to the bottom;
        y - horizontal, increasing to the right.
        :return: nested list (matrix) the size of initialized board size
        """
        self.__board = [["000" for row in range(self.board_size)]
                                       for col in range(self.board_size)]
        self.__occupancy_board = [["0" for row in range(self.board_size)]
                        for col in range(self.board_size)]
        return self.__board

    def draw_board(self) -> None:
        """
        Prints square board showing occupancy of each square with units
        """
        print(end="")
        for row in self.__board:
            print(" ".join(row))
        print("\n", end="")

    def add_team(self, team: tc.Team) -> None:
        """
        Adds the selected team to the board.
        Assigns all units their respective coordinates x, y

        First team is placed on top
        Second team is placed on bottom
        """
        self._team_count += 1
        if self._team_count == 1:
            row = 0
        elif self._team_count == 2:
            row = self.board_size - 1
        else:
            raise ValueError("Only 2 teams supported.")

        for i, unit in enumerate(team.unit_list_inst):
            self.__board[row][i] = unit.symbol + team.symbol
            unit.x = row
            unit.y = i

    def get_board(self, team: tc.Team) -> list:
        """
        Updates the team's units' positions without clearing the previous ones
        :param team: which team's units' positions to update
        :return: the board with units in new positions
        """
        for unit in team.unit_list_inst:
            self.__board[unit.x][unit.y] = unit.symbol + team.symbol
            self.__occupancy_board[unit.x][unit.y] = team.symbol
        return self.__board

    def get_occupancy_board(self) -> list[list[str]]:
        """
        Returns board with occupancy of each square defined with string
        """
        return self.__occupancy_board

if __name__ == "__main__":
    help(Board)