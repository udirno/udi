# Battleship Game

We are implementing the game of Battleship. If you've never played Battleship you can play it online at [battleship.org](https://www.battleshiponline.org/). 

The board size and the ships used in the game are specified in a configuration file using the following format

```
num_rows num_cols 
first_ship_name first_ship_length
second_ship_name second_ship_length
third_ship_name thrid_ship_name
...
```
A round of the Battleship game starts by reading the configuration file and a random seed which provides repeatable behvior to the random number generator. The random number generator makes it almost impossible to guess or predict the the moves performed by the non-human players. The three non-human players to choose from are the Cheating Ai, the Random Ai, and the Search and Destroy Ai. Each of these Ai uses a different strategy to try and beat the opponent which can either be the user or another non-human player. 
The Cheating Ai will play a perfect game without missing a shot. The Random Ai fires at random locations and is unpredictable. Search and Destroy Ai fires randomly until the first hit after which it uses strategy to destroy the rest of the ship.
However, if any of the non-human players use identical strategies in two different rounds, we want those rounds to produce identical board positions. This helps with Software Testing; we can capture the board positions of a few reference rounds, and validate any other implementation of the game *by comparing this to what we want the non-human players employ the same strategy in two rounds of the game unpredictable by other players. However, , and we want them to behave the same way in all  the players are not necessarily human,  
Refactored code has preserves the original functionality???* 
All players start with the same boards and ships and take turns playing the game, and recording their score. A HumanPlayer can choose to play against another HumanPlayer, or one of the three AiPlayers. Note that HumanPlayer places ships differently from the AI players but all AI players place ships the same way, but differently from the human player. The HumanPlayer will then be asked if they want to place their first ship horizontally or vertically (any prefix of horizontal or vertical is accepted). Next, they will be asked for the position where they wish to place their ship. If the position entered is invalid i.e. off the board or in the incorrect format they will be asked again.
Once all the ships are placed the game begins. The players will alternate giving their firing locations. Depending on whether they hit, miss, or destroy a ship a message will be displayed. The game will end when one player destroys all the other player's ships. 

Design a game of Battleship - [battleship.org](https://www.battleshiponline.org/).

## High Level Design
Since players play the game by placing ships on the board, we will start with 4 main classes: ```Game```, ```Player```, ```Board```, ```Ship```. We will put each class must be in its own file, and use type hints on function parameters and return types.   


### Configuration file 

Contains information about the board and ships:


Ship names will begin with X, O, or * [the hit, miss, and blank characters]

Example configuration file:

```
20 13
Anaconda 8
RaceCar 3
SkyScraper 12
Banana 6
```
**Note:** The length of the ship cannot be larger than one of the board's dimensions

### Players

For each player in the game
 
 1. Ask player for their name (name must be unique otherwise keep asking for a new name)
 2. Ask them where they want to place each ship
 	1. Place ships in the order they are found in the configuration file.
	* First, ask whether to place the ship **horizontal or vertical?** 
		* Any prefix of horizontal or vertical should be accepted
	* Ask for the coordinate they would like to place the ship in the form **row, col**
		* Horizontal ships are placed left to right 
		* Vertical ships are placed top to bottom. 
		* 
If the user enters invalid input anywhere along the way they should be told what they did wrong and then you start anew at step 2.2

The Battleship game can be divided into two players: Human Players and non-human players. In the player directory there are two similar classes:  ```player.py``` and ```human_player.py```. 

**player.py** - Has abstract methods to gather information from the user: 
```get_name_from_player(self, other_players: Iterable["Player"])``` gets the player's name; ```get_ship_start_coords(self, ship_: Ship, orientation_: Orientation)``` checks if the coordniate the user enters for where to place the respective is valid i.e. does it fit on the board; Assuming the prefixes for the input are valid ```get_ship_orientation(self, ship_: Ship)``` returns if the ship is to be oriented horizontally or vertically; ```get_move(self, opponent : "Player")``` returns the coordinate for the user's first firing location.

These methods are abstract because this information is gathered from the user so they are defined in the ```human_player.py``` class. The functions that are defined in this class are only the ones that are unique for the non-human human players. The ```get_ship_placement(self, ship_ : Ship)``` gets start cell and orientation for the ship that fits on the board. The ```change_strategy(self, move: Move, score_msg: str)``` function is defined later but passed here. Finally, the ```take_turn(self, opponent: "Player")``` function is used to alternate turns between players and this method also calls the ```change_strategy``` function.

**human_player.py** - This class takes the ```Player``` object as an argument and includes the definitions for all but the three non-human player methods in ```player.py```

### Ships

The two ship classes are ```ship.py``` and ```ship_placement.py```

**ship.py** - Creates a ```Ship``` object with attributes ```ship_name``` and ```ship_len```

**ship_placement.py** - Has the function ```get_ship_end_coords``` which returns the coordinate where the ship ends. This is needed for determining when a ship is completely destroyed.

	
	

	


### The Gameplay Loop

On each players turn

1. Ask them for the location that they want to fire at in the form row, col. If they enter an invalid firing location tell them what is wrong with their input and continue to ask them for a new location they enter a valid location.
2. Shoot that spot
	* Display Miss if they missed
	* Display You hit {player_name}'s {ship_name} if you hit a ship
	* Display You destroyed {player_name}'s {ship_name} if you destroyed it.  
3. Switch to the next player's turn.

The game ends when all of a player's ships have been destroyed. A ship is destroyed when all of its sections have been hit.

#### Invalid Firing Locations

A Firing Location is invalid if

1. The input is not in the form row, col. 
```
{user_input is not a valid location.\n Enter the firing location in the form row, column
```
2. Either row or col is not an integer
```
row: Row should be an integer. {row} is NOT an integer.
col: Column should be an integer. {col} is NOT an integer.
```
3. The location is out of bounds
```
{row}, {col} is not in bounds of our {num_rows} X {num_cols} board.
```
4. The location has already been fired at   
```
 You have already fired at {row}, {col}
```

### Overview

* Read the configuration file 
	* andom seed which provides repeatable behvior to the random number generator. The random number generator makes it almost impossible to guess or predict the the moves performed by the non-human players. However, if the non-human players use identical strategies in two different rounds, we want those rounds to produce identical board positions. This helps with Software Testing; we can capture the board positions of a few reference rounds, and validate any other implementation of the game by comparing this we want two he non-human players employ the same strategy in two rounds of the game unpredictable by other players. However, , and we want them to behave the same way in all  the players are not necessarily human,  
Refactored code has preserves the original functionality

* Start with a base Player class in players/player.py
    * All players are derived from Player.
    * They all start with the same boards and ships. They all use the boards the same way, place ships on the board, take turns to play the game, and record they score in the same way. So use common Player.place_ship(), Player.take_turn(), and Player.record.score()
    * Even though all player subclasses get player name, ship orientation, ship co-ordinate, and next move, they perform those actions in different ways. So add @abc.abstractmethod s Player.get_player_name(), Player.get_ship_orientation(), Player.get_ship_start_coords(), and Player.get_move(). This will force all sub classes use the same signature for all those functions.
* Actual players derive from the Player class - each has its own file
    * HumanPlayer and AiPlayer derive from Player, i.e Player ← (HumanPlayer, AiPlayer). HumanPlayer  is in the same directory, players, but in its own file human_player.py 
        * HumanPlayer places ships differently from the AI players, so use HumanPlayer.get_ship_orientation() and HumanPlayer.get_ship_start_coord()
    * All AI players derive from Player, i.e  Player ← AiPlayer ← (RandomAi, CheatingAi, SearchDestroyAi). They are all in the same directory players/ai in separate files ai_player.py, random_ai.py, cheating_ai.py, and search_destroy_ai.py 
        * All AI players place ships the same way, but differently from the human player. So use AiPlayer.get_ship_orientation() and AiPlayer.get_ship_start_coord()
* Ship.size to Ship.length
* Board,get/set_content to Board.get/set_mark
* Cell to Move
* New ShipPlacement class

