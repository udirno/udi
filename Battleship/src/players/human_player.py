import random
from typing import Iterable
from src.ship import Ship
from src.orientation import Orientation
from src.board import Board, ShipBoard
from src.move import Move, MoveError
from src.players.player import Player

class HumanPlayer(Player):
    def __init__(self, num : int, all_players: Iterable["Player"],
                 ships_ : Iterable["Ship"], num_rows_ : int, num_cols_ : int,
                 blank_char_: str) -> None:
        super().__init__(num, all_players, ships_, num_rows_, num_cols_, blank_char_)

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input(f'Player {self.player_num + 1} please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def get_ship_orientation(self, ship_ : Ship) -> Orientation:
        while True:
            orientation = input(
                f'{self.name} enter horizontal or vertical for the orientation of {ship_.name} which is {ship_.length} long: ')
            orientation = orientation.lower()
            prefixes_hor = ('h', 'hori', 'horiz', 'horizontal')
            prefixes_ver = ('v', 'vert', 'verti', 'vertical')
            if orientation.startswith(prefixes_hor) == True:
                return Orientation.HORIZONTAL
            elif orientation.startswith(prefixes_ver) == True:
                return Orientation.VERTICAL
            else:
                print('ERROR: you must enter either "horizontal" or "vertical".')


    ''' Get start cell and orientation for the ship that fits on the board'''
    def get_ship_start_coords(self, ship_: Ship, orientation_: Orientation):
        while True:
            str_cell = input(
                f'{self.name}, enter the starting position for your {ship_.name} ship ,which is {ship_.length} long, in the form row, column:')
            try:
                move = Move.from_str(str_cell)
                return move.row, move.col
            except MoveError as err:
                print(err)

    def get_move(self, board_: Board) -> Move:
        str_move = input(f'{self.name}, enter the location you want to fire at in the form row, column: ')
        return Move.from_str(str_move)



