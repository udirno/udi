from typing import Iterable
from src.move import Move, MoveError
from src.board import Board, ShipBoard
from src.ship import Ship
from src.ship_placement import ShipPlacement
from src.orientation import Orientation
import abc

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
                 blank_char_: str) -> None:
        self.blank_char = blank_char_
        self.player_num = num + 1
        self.name = self.get_name_from_player(other_players)
        self.scanning_board = Board(num_rows, num_cols, blank_char_)
        self.ship_board = ShipBoard(num_rows, num_cols, ships, blank_char_)
        print(f'{self.name}\'s Placement Board\n {self.ship_board}')
        for ship in ships:
            ship_placement = self.get_ship_placement(ship)
            self.ship_board.place_ship(ship_placement)
            print(f'{self.name}\'s Placement Board\n {self.ship_board}')

    def __str__(self) -> str:
        return self.name

    @abc.abstractmethod
    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        ...

    @abc.abstractmethod
    def get_ship_start_coords(self, ship_: Ship, orientation_: Orientation):
        ...

    @abc.abstractmethod
    def get_ship_orientation(self, ship_: Ship) -> Orientation:
        ...

    @abc.abstractmethod
    def get_move(self, opponent : "Player") -> Move:
        ...

    ''' Get start cell and orientation for the ship that fits on the board'''
    def get_ship_placement(self, ship_ : Ship) -> ShipPlacement:
        orientation = self.get_ship_orientation(ship_)
        row_start, col_start = self.get_ship_start_coords(ship_, orientation)
        return ShipPlacement(ship_, orientation, row_start, col_start)

    def change_strategy(self, move: Move, score_msg: str):
        pass

    def take_turn(self, opponent: "Player") -> None:
        move = None
        while True:
            try:
                move = self.get_move(opponent)
                score_msg = move.make(self.scanning_board, opponent.name, opponent.ship_board)
                self.change_strategy(move, score_msg)
                return
            except MoveError as err:
                print(err)