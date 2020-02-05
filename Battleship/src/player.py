from typing import Iterable, Tuple
from .board import Board
from .ship import Ship
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
        self.ship_board = Board(num_rows, num_cols, blank_char)
        self.hit_board = Board(num_rows, num_cols, blank_char)
        self.name = self.get_name_from_player(other_players)
        self.ship_placements = []
        for ship in ships:
            row, col, orientation = self.get_ship_placement(ship,
                                                            self.ship_board)
            self.ship_placements.append((row, col, orientation))
            self.ship_board.place(ship, row, col, orientation)
            print("Ship Placement Board:\n", self.ship_board)

        print("Hit Board:\n", self.hit_board)

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input(f'Player {self.player_num} please enter your name: ')
            print("Ship Placement Board:\n", self.ship_board)
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def get_ship_placement(self, ship : "Ship", board : "Board") -> Tuple[int, int, str]:
        while True:
            # get ship's placement as oriantation and starting co-ordinate
            orientation = self.get_ship_orientation(ship)
            row, col = self.get_ship_coordinate(ship, board)

            # Check if the ship can be placed on the board with the given
            # placement (row, col, and oriendtation). If it is a valid
            # placement we are ready to proceed, otherwise retry
            if board.can_place(ship, row, col, orientation):            
                return (row, col, orientation)
            else:
                print(f'ERROR: {ship.name} overlaps with another ship if placed {orientation}ly at {row}, {col}.')
    '''
    Check if placing ship at row, col with orientation is valid, i.e the ship
    does not stick out of the board, and it does not overlap with any other 
    ships that are already on the board
    '''
    def valid_placement(ship, row, col, orientation, board):
        # TBD
        return
        True

    def get_ship_orientation(self, ship : Ship):
        # TBD: check prefix with if...
        while True:
            orientation = input(f'{self.name} enter horizontal or vertical for the orientation of {ship.name} , which is {ship.size} long:')
            orientation = orientation.lower()
            prefixes_hor = ('h', 'hori', 'horiz', 'horizontal')
            prefixes_ver = ('v', 'vert', 'verti', 'vertical')
            if orientation.startswith(prefixes_hor) == True:
                orientation = 'horizontal'
                return orientation
            elif orientation.startswith(prefixes_ver) == True:
                orientation = 'vertical'
                return orientation
            else:
                print('ERROR: you must enter either "horizontal" or "vertical".')
    

    def get_ship_coordinate(self, ship : Ship, board : Board):
        # TBD check python formatted input int, int otherwise ask again...
        # row, col = input('Where would you place ship {ship.name}  (row, col) ?')
        while True:
            inputs = input(
                f'{self.name}, enter the starting position for your {ship.name} ship , which is {ship.size} long, in the form row, column:').split(
                ',')
            try:
                co_ordinate = [int(x.strip()) for x in inputs]
            except:
                (ValueError, TypeError)
                continue
            if len(co_ordinate) != 2:
                print(f'ERROR: you must enter two numbers separated by a comma.')
            elif not board.is_in_bounds(*co_ordinate):
                print(f'ERROR: co-ordiante {co_ordinate} falls outside the {board.num_rows}x{board.num_cols} board.')                
            else:
                break
        return co_ordinate

            

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
