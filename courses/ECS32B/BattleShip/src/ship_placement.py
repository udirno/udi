from src.orientation import Orientation
from src.ship import Ship

import abc

class ShipPlacement(object):
    def __init__(self, ship_: Ship, orientation_: Orientation, row_start_: int, col_start_: int) -> None:
        self.ship = ship_
        self.orientation = orientation_
        self.row_start, self.col_start = row_start_,  col_start_
        self.row_end, self.col_end = self.get_ship_end_coords(ship_, orientation_, row_start_, col_start_)
        #print(f'start ({self.row_start}, {self.col_start}), end ({self.row_end}, {self.col_end})')
        if self.row_end is None:
            raise NotImplementedError(f'Placing ships {orientation_} is not supported yet.')


    @abc.abstractmethod
    def get_ship_end_coords(self, ship: Ship, orientation: Orientation, row_start_: int, col_start_: int):
        row_end_,col_end_ = row_start_, col_start_
        if orientation == Orientation.HORIZONTAL:
            col_end_ = col_start_ + ship.length - 1
        elif orientation == Orientation.VERTICAL:
            row_end_ = row_start_ + ship.length - 1
        else:
            row_end_ = col_end_ = None
        return row_end_, col_end_




