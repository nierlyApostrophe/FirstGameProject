# Army Game Project

***A game for two players, which consists of two types of units.
Set a board size, the amount of total units, and the type of each unit in your team.***

## How to play?

The game goes on infinitely until all the units of a Team are dead.

1. You will be asked the amount of total units per team; 
then you will be asked to input the amount of infantry (each team decides themselves).  
1. This is the end of initialization, and where the main loop begins.
1. You will then see the X and Y axes as well as the created board with both teams' units.  
   **Team 1**:  
1. You will be presented with a choice: **to move or to attack**.
1. After the choice's been made you have to input the number, 
which corresponds to the unit you will select from an array of units.  
1. You then have to enter the **delta coordiantes**, which decide which square are you
moving to/attacking.  
1. Then the queue goes to **Team 2** and all the previous steps of the main loop repeat.


## Files' roles

### `unit_create.py` - contains all info about unit objects;

Any given unit cannot attack by itself, and additional logic is needed. Thus `unit_create.py`
does not contain methods to attack another unit and such logic is implemented in `main.team_turn()`.  
Project currently utilizes two types of units: infantry and cavalry.
More units can be added via the `unit_create.py`.  
However, more logic is needed to be implemented in `main.py` to account for new units.

### `team_create.py` - contains all info about team object. Uses unit_create.py in itself;


### `board_create.py` - contains all info about board object. Uses team_create.py in itself;


### `main.py` - contains all the logic. 

The way the game goes is set in `team_turn()` and `main()`.  
The way to assign units to each team is set in `add_units()`.  
The project supports validation for all inputted values. 
The validation is described in the next three functions:  
* `is_valid_type()`
* `ret_of_type()`
* `ret_valid()`
