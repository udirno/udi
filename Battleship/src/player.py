from typing import Iterable, Tuple
from .ship import Ship
from .cell import Cell, CellError
from .board import Board, ShipBoard

'''
In the Player class we keep information regarding 
- player's name
- ship placement board
- target hit board
- ship placements (orientation, co-ordinates etc.)
'''

class Player(object):
    def __init__(self, num : int, other_players: Iterable["Player"],
                 ships: Iterable["Ship"], num_rows: int, num_cols: int,
                 blank_char: str) -> None:
        self.player_num = num
        self.name = self.get_name_from_player(other_players)
        self.scanning_board = Board(num_rows, num_cols, blank_char)
        self.ship_board = ShipBoard(num_rows, num_cols, ships, blank_char)
        print(f'{self.name}\'s Placement Board\n {self.ship_board}')
        for ship in ships:
            start_cell, orientation = self.get_ship_placement(ship, self.ship_board)
            self.ship_board.place_ship(ship, start_cell, orientation)
            self.ship_board.ship_placements.append((start_cell, orientation))
            print(f'{self.name}\'s Placement Board\n {self.ship_board}')

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input(f'Player {self.player_num} please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    ''' Get start cell and orientation for the ship that fits on the board'''
    def get_ship_placement(self, ship: "Ship", board: "Board"):
        orientation = ship.get_orientation(self.name)
        while True:
            scell = ship.get_start_cell(self.name)

            # Check if the ship can be placed on the board at the start_cell in the given orientation.
            # If not, retry until a valid start cell is found
            if board.ship_fits(ship, scell, orientation):
                return (scell, orientation)
            else:
                print(
                    f'ERROR: {ship.name} overlaps with another ship if placed {orientation}ly at {scell.row}, {scell.col}.')

    def __str__(self) -> str:
        return self.name

    def take_turn(self, opponent: "Player") -> None:
        tcell = None
        while True:
            try:
                tcell = self.get_target()
                break
            except CellError as error:
                print(error)
        scanning_mark = self.scanning_board.get_content(tcell)
        opponent_ship = opponent.ship_board.get_ship(tcell)
        new_scanning_mark = 'O' if opponent_ship == None else 'X'
        self.scanning_board.set_content(tcell, new_scanning_mark, False)
        if opponent_ship == None:
            message = 'Miss'
        elif opponent.ship_board.intact_cell_count(opponent_ship, self.scanning_board) == 0:
            message = f'You destroyed {opponent.name}\'s {opponent_ship.name}'
        else:
            message = f'You hit {opponent.name}\'s {opponent_ship.name}'
        print(message)


    def get_target(self) -> "Cell":
        str_cell = input(f'{self.name}, enter the location you want to fire at in the form row, column: ')
        return Cell.from_str(str_cell)
