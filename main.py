import team_create as tc
import board_create as bc
import unit_create as uc

from time import sleep
from typing_extensions import Any

def is_valid_type(val: Any,
                  type_check: Any) -> bool:
    """
    Checks if a value could be made into the other type
    :param val: a value to check
    :param type_check: a type to check the transformation into
    :return: True if transformable, False if not.
    """
    try:
        type_check(val)
        return True
    except ValueError:
        return False

def ret_of_type(val: Any,
                type_check: Any,
                inp_str: str="Input: ") -> Any:
    """
    Returns the value of the set type. Repeatedly asks
    for an input until is able to transform value to the type.
    :param val: a value to check
    :param type_check: a type to transform into
    :param inp_str: an input string during the value request
    :return: returns validated value of set type
    """
    while not is_valid_type(val, type_check):
        val = input(inp_str)
    return type_check(val)

def ret_valid(min_buf: Any,
              max_buf: Any,
              type_check: Any,
              inp_str: str="Input: ",
              buf: Any=-1) -> Any:
    """
    Requests a value input and returns the value of set type
    validated over the condition min_buf < value < max_buf
    :param min_buf: the low buffer border
    :param max_buf: the high buffer border
    :param type_check: a type for a value
    :param inp_str: a string to be displayed during a value request
    :param buf: a buffer to which the value will be written and conditioned from
    :return: value of type type_check that passed the condition
    """
    while not min_buf < buf < max_buf:
        value: str | type = input(inp_str)
        buf = ret_of_type(value,
                          type_check,
                          f"Wrong type! "
                          f"Expected type {type_check} ({min_buf+1}-{max_buf-1}): ")
    return buf

##############################################

def add_units(team: tc.Team,
              unit_amount: int,
              inf_amount: int) -> None:
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

def option_menu() -> int:
    """
    Makes you select between different options via input.
    Checks if the input is an int of set
    :return: 1 or 2
    """
    return ret_valid(0, 4, int, "\nChoose what to do:\n"
                                                        "1. Move your unit\n"
                                                        "2. Attack enemy unit\n"
                                                        "3. Exit the program\n")

def new_delta_coords() -> tuple[int, int]:
    """
    Requests two inputs for delta x, delta y
    :return: tuple of integers
    """
    return (ret_of_type(input("Enter delta X: "), int, "Enter delta X: "),
            ret_of_type(input("Enter delta Y: "), int, "Enter delta Y: "))

def team_turn(option: int,
              board: bc.Board,
              team: tc.Team,
              enemy_team: tc.Team) -> bool | None:
    """
    Performs a turn over a unit for a selected team
    (i.e. unit selection, movement, attack)
    :param option: refers to the main.option_menu()
    :param board: current board
    :param team: which team's turn it is
    :param enemy_team: team, which units will be attacked
    :return: returns False if new coordinates are out of bounds / True if new coordinates were accepted
    """

    if option == 3:
        print("Exiting the program")
        exit()

    unit_id: int = ret_valid(0,
                            len(team.unit_list_inst) + 1,
                            int,
                            f"\nEnter unit's number (1 - {len(team.unit_list_inst)}): ") - 1

    if option == 1:
        delta_x, delta_y = new_delta_coords()
        new_x = delta_x + team.unit_list_inst[unit_id].x
        new_y = delta_y + team.unit_list_inst[unit_id].y
        if 0 > new_x > board.board_size and 0 > new_y > board.board_size:
            print(f"Invalid input; coordinates out of bounds: 0 <= (x, y) <= {board.board_size-1}")
            return False
        if board.get_occupancy_board()[new_x][new_y] == "0":
            team.unit_list_inst[unit_id].move(delta_x,
                                              delta_y,
                                              board.board_size)
            return True
        print("Unable to move to an already occupied square")
        return False

    elif option == 2:
        delta_x, delta_y = new_delta_coords()
        attack_x = delta_x + team.unit_list_inst[unit_id].x
        attack_y = delta_y + team.unit_list_inst[unit_id].y
        if 0 > attack_x or attack_x > board.board_size or 0 > attack_y or attack_y > board.board_size:
            print(f"Invalid input; coordinates out of bounds: 0 <= (x, y) <= {board.board_size-1}")
            return False
        if board.get_occupancy_board()[attack_x][attack_y] == enemy_team.symbol:
            for enemy_unit in enemy_team.unit_list_inst:
                if enemy_unit.x == attack_x and enemy_unit.y == attack_y:
                    enemy_unit.health -= team.unit_list_inst[unit_id].damage
                    print(f"Successfully attacked {enemy_unit.name} at ({enemy_unit.x}, {enemy_unit.y})\n")
                    return True
        print(f"Failed to find an enemy at ({attack_x}, {attack_y})\n")
        return False

    else:
        print("Invalid choice!")

def team_info(team: tc.Team):
    """
    Prints all info on all units of a selected team
    :param team: a team to show info about
    """
    i = 1
    for unit in team.unit_list_inst:
        print(f"{i}. Team{team.symbol} unit: {unit.name}, position: {unit.x, unit.y}, "
              f"health: {unit.health}, damage: {unit.damage}, moves: {unit.moves}")
        i += 1
    print()

def main() -> None:
    board_size = ret_valid(bc.Board.min_board_size - 1,
                           bc.Board.max_board_size + 1,
                           int,
                           f"Enter the board size ({bc.Board.min_board_size}-{bc.Board.max_board_size}): ")
    new_board: bc.Board = bc.Board(board_size)

    unit_amount = ret_valid(0,
                            board_size + 1,
                            int,
                            "Enter the amount of units per team: ")

    # creating teams, adding units to them
    team1: tc.Team = tc.Team(unit_amount)
    team1.symbol = "1"
    team2: tc.Team = tc.Team(unit_amount)
    team2.symbol = "2"
    teams: tuple = (team1, team2)
    for team in teams:
        inf_amount = ret_valid(-1,
                               unit_amount + 1,
                               int,
                               f"Team {team.symbol}: How much infantry troops do you want "
                               f"(0-{unit_amount}). Cavalry will be decided as the rest: ")
        add_units(team, unit_amount, inf_amount)

    new_board.add_team(team1)
    new_board.add_team(team2)

    print("0————————>Y\n|\n|\n/\nX")
    game_queue: bool = True

    while True:
        for team in teams:
            team.health_check()
            if not team.unit_list_inst:
                print(f"Team {team.symbol} has lost!")
                exit()
            new_board.get_board(team)
        new_board.get_occupancy_board()
        new_board.draw_board()
        sleep(1)
        if game_queue:
            print("Turn of Team 1!")
            team_info(team1)
            sleep(0.5)
            team_info(team2)
            while not team_turn(option_menu(), new_board, team1, team2):
                pass
            game_queue = False
        else:
            print("Turn of Team 2!")
            team_info(team2)
            sleep(0.5)
            team_info(team1)
            while not team_turn(option_menu(), new_board, team2, team1):
                pass
            game_queue = True
        new_board.empty_board()

if __name__ == "__main__":
    main()