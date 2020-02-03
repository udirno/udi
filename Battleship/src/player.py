from typing import Iterable
from .move import Move, MoveError
from .board import Board
'''
In the Player class we keep information regarding 
- player's name
- ship placement board
- target hit board
- ship placements (orientation, co-ordinates etc.)
'''

class Player(object):
    def __init__(self, ships: Iterable[Ship], num_rows: int, num_cols: int, blank_char: str) -> None:
        self.name = self.get_name_from_player(other_players)
        self.ship_placement_board = Board(num_rows, num_cols, blank_char)
        self.target_hit_board = Board(num_rows, num_cols, blank_char)
        self.ship_placements = []
        for ship in ships:
            row, col, orientation = self.get_ship_placement(ship, board)
            self.ship_placements.append((row, col, orientation))
            self.ship_placement_board.place(ship, row, col, orientation)

    def self.get_name_from_player(other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def self.get_ship_placement(ship : Ship, board : Board) -> Tuple:
        while True:
            # get ship's placement as oriantation and starting co-ordinate
            orientation = get_ship_orientation(ship)
            row, col = get_ship_coordinate(ship)

            # Check if the ship can be placed on the board with the given
            # placement (row, col, and oriendtation). If it is a valid
            # placement we are ready to proceed, otherwise retry
            if board.can_place(ship, row, col, orientation):            
                return (row, col, orientation)

    '''
    Check if placing ship at row, col with orientation is valid, i.e the ship
    does not stick out of the board, and it does not overlap with any other 
    ships that are already on the board
    '''
    def valid_placement(ship, row, col, orientation, board):
        # TBD
        retrun
        True

    def get_ship_orientation(ship):
        # TBD: check prefix with if...
        orientation = input('How would you place ship {ship.name} (horizontal or vertical) ?:')
        orientation.lower()
        prefixes_hor = ('h', 'hori', 'horiz', 'horizontal')
        prefixes_ver = ('v', 'vert', 'verti', 'vertical')
        if orientation.startswith(prefixes_hor) == True:
            orientation = 'horizontal'
            return orientation
        elif orientation.startswith(prefixes_ver) == True:
            orientation = 'vertical'
            return orientation
        else:
            print(orientation, ' does not represent an Orientation')

def get_ship_coordinate(ship):
        # TBD check python formatted input int, int otherwise ask again...
        # row, col = input('Where would you place ship {ship.name}  (row, col) ?')
        row, col = [int(x) for x in input("Where would you place ship {ship.name} (row, col) ?").split(,)] #store in list?
        return (row, col)

    def __str__(self) -> str:
        return self.name

    def take_turn(self, the_board: "Board") -> None:
        while True:
            try:
                move = self.get_move()
                move.make(the_board)
                return
            except MoveError as error:
                print(error)

    def get_move(self) -> "Move":
        str_move = input(f'{self} enter where you want to play in the form row, col: ')
        return Move.from_str(self, str_move)