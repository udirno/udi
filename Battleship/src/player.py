from typing import Iterable, Tuple
from .ship import Ship
from .cell import Cell, CellError
from .board import Board

'''
In the Player class we keep information regarding 
- player's name
- ship placement board
- target hit board
- ship placements (orientation, co-ordinates etc.)
'''


class Player(object):
    def __init__(self, num: int, other_players: Iterable["Player"],
                 ships: Iterable["Ship"], num_rows: int, num_cols: int,
                 blank_char: str) -> None:
        self.player_num = num
        self.ship_board = Board(num_rows, num_cols, blank_char)
        self.hit_board = Board(num_rows, num_cols, blank_char)
        self.name = self.get_name_from_player(other_players)
        self.ship_placements = []
        for ship in ships:
            cell, orientation = self.get_ship_placement(ship, self.ship_board)
            self.ship_placements.append((cell, orientation))
            self.ship_board.place_ship(ship, cell, orientation)
            print(f'{self.name}\'s Placement Board\n {self.ship_board}')

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        already_used_names = set([player.name for player in other_players])
        while True:
            name = input(f'Player {self.player_num} please enter your name: ')
            print('{self.name}\'s Placement Board\n {self.ship_board}')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def get_ship_placement(self, ship: "Ship", board: "Board") -> Tuple["Cell", str]:
        while True:
            # get ship's placement as oriantation and starting co-ordinate
            orientation = self.get_ship_orientation(ship)
            cell = self.get_ship_start(ship, board)

            # Check if the ship can be placed on the board with the given
            # placement (row, col, and oriendtation). If it is a valid
            # placement we are ready to proceed, otherwise retry
            if board.ship_fits(ship, cell, orientation):
                return (cell, orientation)
            else:
                print(
                    f'ERROR: {ship.name} overlaps with another ship if placed {orientation}ly at {cell.row}, {cell.col}.')

    def get_ship_orientation(self, ship: Ship) -> str:
        while True:
            orientation = input(
                f'{self.name} enter horizontal or vertical for the orientation of {ship.name} , which is {ship.size} long:')
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

    def get_ship_start(self, ship: "Ship", board: "Board") -> "Cell":
        # TBD check python formatted input int, int otherwise ask again...
        # row, col = input('Where would you place ship {ship.name}  (row, col) ?')
        while True:
            str_cell = input(
                f'{self.name}, enter the starting position for your {ship.name} ship , which is {ship.size} long, in the form row, column:')
            try:
                cell = Cell.from_str(str_cell)
                print(f'return {cell.row}, {cell.col} from {str_cell}')
                return cell
            except CellError:
                pass

    def __str__(self) -> str:
        return self.name

    def take_turn(self, opponent: "Player", opponent_board: "Board") -> None:
        while True:
            try:
                tcell = self.get_target()
                tmark = 'O'
                self.hit_board.occupy(tcell, tmark)
                tmark_old = opponent_board.contents[tcell.row][tcell.col]
                if tmark_old in set('O', blank_char):
                    print('Miss')
                else:
                    tmark = 'X'
                    # opponent_ship = opponent_board.get_ship_at(tcell)
                    opponent_ship = Ship("fake", 4)
                    if True:
                        print(f'You destroyed {opponent.name}\'s {opponent_ship.name}')
                    else:
                        print(f'You hit {opponent.name}\'s {opponent_ship.name}')
                    opponent_board.occupy(tcell, tmark)
                return
            except CellError as error:
                print(error)

    def get_target(self) -> "Cell":
        str_cell = input(f'{self.name} Bob, enter the location you want to fire at in the form row, column: ')
        return Cell.from_str(str_cell)