import copy
from typing import Iterable, Tuple
from .cell import Cell, CellError
class Ship(object):
    def __init__(self, ship_name : str, ship_len : int) -> None:
        self.name = ship_name
        self.size = ship_len

    def get_orientation(self, player_name: str) -> str:
        while True:
            orientation = input(
                f'{player_name} enter horizontal or vertical for the orientation of {self.name} which is {self.size} long:')
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

    def get_start_cell(self, player_name: str) -> "Cell":
        # TBD check python formatted input int, int otherwise ask again...
        # row, col = input('Where would you place ship {ship.name}  (row, col) ?')
        while True:
            str_cell = input(
                f'{player_name},enter the starting position for your {self.name} ship , which is {self.size} long, in the form row, column:')
            try:
                cell = Cell.from_str(str_cell)
                print(f'return {cell.row}, {cell.col} from {str_cell}')
                return cell
            except CellError as error:
                print(error)

    def get_end_cell(self, scell: "Cell", orientation: str) -> "Cell":
        ecell = copy.copy(scell)
        if orientation == 'horizontal':
            ecell.col = scell.col+self.size-1
        elif orientation == 'vertical':
            ecell.row = scell.row+self.size-1
        return ecell

