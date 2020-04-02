# Battleship Game

We are implementing the game of Battleship. If you've never played Battleship you can play it online at [battleship.org](https://www.battleshiponline.org/). 

The Battleship game is played between two players on a board where each player places their ships. Information about the size of the board (number or rows and columns), and the ships (names and sizes) are specified in configuration file. For example:

```
20 13
Anaconda 8
RaceCar 3
SkyScraper 12
Banana 6
```

The Battleship game starts by reading the configuration file and a random seed. The random seed is used for non-human players which is described below.

The players can be either human or non-human (AI). There are three diffrent types of AI players to choose from: Cheating AI, Random AI, and the Search-and-Destroy AI. Each type of AI player use a different strategy to try and beat the opponent which can either be either a human another AI player. 


Cheating AI plays a perfect game without missing a shot. Random AI fires at random locations and is unpredictable. Search and Destroy AI fires randomly until the first hit, after which it switches to destroy mode and uses strategy to try and destroy the rest of the ship.

We implement random firing using a random number generator. The random number generator makes it almost impossible to guess or predict the the moves performed by the AI players. However, even though random moves are not **predictable** we want the games to be **repeatable**, i.e. replay of the same game should produce the same sequence of random moves. The games are made repeatable by making the random number generator during replay use the same seed (an integer) as the original game. This explains why a seed is provided while staring the game.

We want the replay to be repeatable to facilitate software testing. We can capture the board positions of a reference game, and validate any other implementation of the game by running them with the same seed and comparing the board positons with the reference game.

However, if any of the non-human players use identical strategies in two different rounds, we want those rounds to produce identical board positions. This helps with Software Testing; we can capture the board positions of a few reference rounds, and validate any other implementation of the game 
 
All players start with the same boards and ships and take turns playing the game, and recording their score. Each player can be of any type: human or one of the  3 AI types. In the beginning, each player places all his or her ships on the board. Every human player places ships the way he or she wants. For each ship the human player specifies the orientation (horizonatal or vertical) and the position of the head of the ship (row and column). The AI players programmatically places all the ships using the same fixed set of rules. 


Once all the ships are placed the game begins. The players will alternate giving their firing locations. Depending on whether they hit, miss, or destroy a ship a message will be displayed. The game will end when one player destroys all the other player's ships and is declared winner. 



## Formal Requirements

### Configuration file 

Ship names will begin with X, O, or * [the hit, miss, and blank characters]


The board size and the ships used in the game are specified in a configuration file using the following format

```
num_rows num_cols 
first_ship_name first_ship_length
second_ship_name second_ship_length
third_ship_name thrid_ship_name
...
```

## High Level Design
Since players play the game by placing ships on the board, we will start with 4 main classes: ```Game```, ```Player```, ```Board```, ```Ship```. We will put each class must be in its own file, and use type hints on function parameters and return types.   



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

**player.py** - The Player class has abstract methods to gather information from the user: 
```get_name_from_player(self, other_players: Iterable["Player"])``` gets the player's name; ```get_ship_start_coords(self, ship_: Ship, orientation_: Orientation)``` checks if the coordniate the user enters for where to place the respective is valid i.e. does it fit on the board; Assuming the prefixes for the input are valid ```get_ship_orientation(self, ship_: Ship)``` returns if the ship is to be oriented horizontally or vertically; ```get_move(self, opponent : "Player")``` returns the coordinate for the user's first firing location.

These methods are abstract because this information is gathered from the user so they are defined in the ```human_player.py``` class. The functions that are defined in this class are only the ones that are unique for the non-human human players. The ```get_ship_placement(self, ship_ : Ship)``` gets start cell and orientation for the ship that fits on the board. The ```change_strategy(self, move: Move, score_msg: str)``` function is defined later but passed here. Finally, the ```take_turn(self, opponent: "Player")``` function is used to alternate turns between players and this method also calls the ```change_strategy``` function.

**human_player.py** - This HumanPlayer class takes the ```Player``` object as an argument and includes the definitions for all but the three non-human player methods in ```player.py```

**ai_player.py** - The AiPlayer class is the base class for the three types of AI players (Random AI, Search and Destroy AI and Cheating AI) so it only has functions that gather information that all three AI's need. These include ```get_random_name(self, other_players: Iterable["Player"])``` which either takes the name the user gives it for the opponent or picks one randomly from a default set. ```get_name_with_prefix``` is used to name the AI player for example as "Random Ai 1".  The ```get_ship_orientation(self, ship_: Ship)``` function picks the orientation of the ship randomly from the list containg the two options: horizontal or vertical. ```get_ship_start_coords(self, ship_: Ship, orientation_: Orientation)``` calculates the start coordinate for the ship based on its orientation. **The start coordinate is always from the top of the ship.**

**random_ai.py** - The RandomAI class takes an AiPlayer object as an argument.```get_name_from_player(self, other_players: Iterable["Player"])``` calls its parent function ```get_name_with_prefix``` to pick a random name from the list. ```firing_locations``` is a list of tuples containing all the coordinates on the board. The ```get_move``` function randomly chooses a coordinate from ```firing_locations``` and then removes it from the list to avoid repetition. 

**cheating_ai.py** - The CheatingAi class takes an AiPlayer object as an argument. It has a ```get_name_from_player(self, other_players: Iterable["Player"])``` method which creates the name for the Cheating Ai. There is also a ```get_move(self, opponent: "Player")``` function which calls the ```get_ship_coordinate``` method to gather the ship locations of the opponent. For the Cheating AI, the ```firing_locations``` become the same as the ```get_ship_coordinate``` locations so that every shot is a guranteed hit. After each turn the firing location is removed from ```firing_locations```. This allows Cheating AI to play a perfect game.

**search_destroy_ai.py** - The SearchDestroy class takes an AiPlayer as an argument. It has a ```get_name_from_player(self, other_players: Iterable["Player"])``` method which creates the name for the Search and Destroy Ai. The ```get_move``` function in this class initially chooses a random firing location. After firint that location is then removed from ```firing_locations```. After the first hit however, the ```self.mode``` changes to "destroy mode". The ```change_strategy(self, move : Move, score_msg : str)``` method is used to switch from **search** to **destroy** mode. There is a ```destroy_locations```double ended queue ```(deque)``` which stores the potential destroy locations by checking the left, right, top, and bottom coordinates of the hit location and adds them to the deque. Note that before adding a coordinate to ```destroy_locations``` the coordinate must also be in ```firing_locations``` so that no coordinate is used multiple times. The next firing location is chosen by using ```popLeft``` on the ```deque``` and continues this process till the whole ship has been destroyed.

### Ships

The two ship classes are ```Ship``` and ```ShipPlacement```

**ship.py** - Creates a ```Ship``` object with attributes ```ship_name``` and ```ship_len```.

**ship_placement.py** - Has the function ```get_ship_end_coords``` which returns the coordinate where the ship ends. This is needed for determining when a ship is completely destroyed.

### Game

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

**orientation.py** - The 

**game.py** - The Game class stores all the information about the game itself. The constructor ... ```pick_player_type``` function gives the user the four player options (Human, or one of the three AI's) to choose from.



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

