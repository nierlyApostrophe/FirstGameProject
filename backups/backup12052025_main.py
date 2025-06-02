# todo
#  "
#  * Додати перевірку зайнятості клітинки іншим юнітом
#  * Додати перевірку (у main.py) на правильність введеної Піхоти (всього юнітів = 5, піхоти = 10)
#  * Додати методи attack(), death() класу Unit
#  * Додати меню вибору дії: хід, атака тощо.
#  "
import team_create as tc
import board_create as bc
import unit_create as uc

def team_turn(board: bc.Board, team: tc.Team) -> None:
    """
    Performs a turn over a unit for a selected team (i.e. unit selection, movement, attack)
    :param board: current board
    :param team: which team's turn it is
    """
    print(team.unit_list)
    team.unit_list_inst[int(input(f"\nEnter unit's number (1 - {len(team.unit_list_inst)}): "))
                         - 1].move(int(input("Enter X: ")),
                                   int(input("Enter Y: ")),
                                   board.board_size)
    for unit in team.unit_list_inst:
        print(f"Team {team.symbol} unit: {unit.name}, position: {unit.x,unit.y}")

def add_units(team: tc.Team, unit_amount: int, inf_amount: int) -> None:
    """
    Adds all units to the selected team
    :param team: Which team to add units to
    :param unit_amount: Total amount of units
    :param inf_amount: Amount of infantry units that will be added
    """
    for i in range(inf_amount):
        team.add_unit(uc.Infantry())
    for i in range(unit_amount - inf_amount):
        team.add_unit(uc.Cavalry())

def valid_check(val,
             condition: bool,
             inp_add: str="",
             err: str="Incorrect amount, enter again",
             inp: str=""
             )-> int | None:
    """
    Repeatedly asks for an input of value until it is valid over the condition.
    :param val: Value to validate
    :param condition: Condition to validate over
    :param inp_add: An addition to the input string
    :param err: Error string
    :param inp: Overwrites the whole input string
    :return: Returns inputted value if the condition is true

    >>> amount = 0
    >>> amount = valid_check(amount, amount < 10, "apples")
    >>> print(amount)
    Input the amount of apples: 6
    6
    Process finished with exit code 0

    >>> amount = 0
    >>> amount = valid_check(amount, amount < 10, "", "Wrong amount!")
    Input the amount: 11
    Wrong amount!
    Input the amount: 6
    6
    Process finished with exit code 0
    """
    _: bool = True
    while _:
        if inp == "":
            inp = "Input the amount"
            if inp_add == "":
                pass
            else:
                inp = f"{inp} of {inp_add}: "
        val = int(input(inp))
        if condition:
            print(f"{err}\n")
        else:
            _ = False
            return val

def main() -> None:
    new_board: bc.Board = bc.Board(int(input("Enter the board size: ")))

    # validating the amount of units per team
    unit_amount: int = 5
    unit_amount = valid_check(unit_amount,
                              (unit_amount > new_board.board_size or unit_amount <= 0),
                              "units per team",
                              f"Number of units must be less or equal to the board size: 1 - {new_board.board_size}")

    # creating teams, adding units to them
    team1: tc.Team = tc.Team(unit_amount)
    team1.symbol = "1"
    inf_amount = 0
    inf_amount = valid_check(inf_amount,
                             inf_amount > unit_amount or inf_amount < 0,
                             err=f"Number of infantry must be less or equal to the total amount of units: 1 - {unit_amount}",
                             inp="Team 1: How much infantry troops do you want (cavalry will be decided as the rest): ")
    add_units(team1, unit_amount, inf_amount)

    team2: tc.Team = tc.Team(unit_amount)
    team2.symbol = "2"
    inf_amount = valid_check(inf_amount,
                             inf_amount > unit_amount or inf_amount < 0,
                             err=f"Number of infantry must be less or equal to the total amount of units: 1 - {unit_amount}",
                             inp="Team 2: How much infantry troops do you want (cavalry will be decided as the rest): ")
    add_units(team2, unit_amount, inf_amount)

    new_board.add_team(team1)
    new_board.add_team(team2)

    print("0--------->Y\n|\n|\n/\nX")
    # Game loop starts here
    new_board.draw_board()
    game_queue: bool = True
    while True:
        new_board.empty_board()
        if game_queue:
            print("Turn of Team 1!")
            team_turn(new_board, team1)
            game_queue = False
        else:
            print("Turn of Team 2!")
            team_turn(new_board, team2)
            game_queue = True
        new_board.get_board(team1)
        new_board.get_board(team2)
        new_board.draw_board()

if __name__ == "__main__":
    main()