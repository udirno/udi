from typing import Iterable, Iterator, List, Tuple
from src.ship import Ship
from src.ship_placement import ShipPlacement

''' Examples of how to iterate over the board
index = 0
every_other = []
for elem in iterable:
    if index%2 == 0:
        every_other.append(elem)
    index += 1

# Alternative 2. Use enumerate and get position information implicitly
every_other = []
for tuple in enumerate(iterable):
    position, elem = tuple
    if position%2 == 0:
        every_other.append(elem)
print(every_other)

b = Board(args to make a board)
for row in b:
  for spot in row:
    do something with spot

#to iterate through instance of board and not through board class
for row in board:
    for spot in row:
        do something with spot
'''
class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str) -> None:
        #2d list of lists
        self.contents = [[blank_char for col in range(num_cols)] for row in range(num_rows)]
        self.blank_char = blank_char

    @property
    def num_rows(self) -> int:
        return len(self.contents)

    @property
    def num_cols(self) -> int:
        return len(self[0])

    def __str__(self) -> str:
        """
          0 1 2
        0 X 0 *
        1 * * 0
        2 O O X
        :return:
        """
        sep = ' ' * max([len(str(self.num_rows)), len(str(self.num_cols))])
        rep = sep + sep.join((str(i) for i in range(self.num_cols)))
        for row_index, row in enumerate(self):
            rep += '\n' + str(row_index) + sep + sep.join(row)
        return rep

    def __iter__(self) -> Iterator[List[str]]:
        return iter(self.contents)

    def __getitem__(self, index: int) -> List[str]:
        return self.contents[index]

    def is_full(self) -> bool:
        return all(
            (space != self.blank_char for row in self for space in row)
        )

    ''' Generator to iterate over the cells of the board '''
    def cells(self, ship: "Ship", scell: "Cell", orientation: str) :
        gen_exp = (Cell(r, c) for c in range(len(self.contents)) for r in range(self.contents[0]))
        return gen_exp

    def get_empty_coordinates(self) -> List[Tuple[int, int]]:
        empty_coords = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self[row][col] == self.blank_char:
                    empty_coords.append((row, col))
        return empty_coords

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.num_rows and
                0 <= col < self.num_cols)

    def is_blank(self, row: int, col: int) -> bool:
        return self.is_in_bounds(row, col) and \
               self.get_mark(row, col) == self.blank_char

    def get_mark(self, row: int, col: int):
        if self.is_in_bounds(row, col):
            return self.contents[row][col]

    '''Place a piece in the cell if it is not occupied or out of bounds; otherwise raise CellError.'''
    def set_mark(self, row: int, col: int, mark: str, check_occupied = True):
        if not check_occupied:
            self.contents[row][col] = mark
        else:
            if not self.is_in_bounds(row, col):
                raise CellError(f'{row}, {col} is not in bounds')
            elif self.get_mark(row, col) != self.blank_char:
                raise CellError(f"location {row}, {col} is already occupied")
            else:
                self.contents[row][col] = mark

''' ShipBoard is derived from Board. It is a board with ships on it. '''
class ShipBoard(Board):
    def __init__(self, num_rows: int, num_cols: int, ships: Iterable["Ship"], blank_char: str):
        super().__init__(num_rows, num_cols, blank_char)
        self.ships = ships
        self.ship_placements = {}


    ''' Check if each cell the ship would occupy on the board is empty, i.e. contains a blank character '''
    def placement_valid(self, ship_placement : ShipPlacement) -> bool:
        result = True
        for r in range(ship_placement.row_start, ship_placement.row_end + 1):
            for c in range(ship_placement.col_start, ship_placement.col_end + 1):
                if not self.is_blank(r, c):
                    result = False
                    break
            if not result:
                break
        return result

    ''' Mark each cell the ship occupies on the board  with the first letter of the ship
    name. Raise CellError if any of those cells are out of bounds or already occupied.
    '''
    def place_ship(self, ship_placement : ShipPlacement) -> None:
        self.ship_placements[ship_placement.ship] = ship_placement
        ship_letter = ship_placement.ship.name[0]
        for r in range(ship_placement.row_start, ship_placement.row_end+1):
            for c in range(ship_placement.col_start, ship_placement.col_end+1):
                try:
                    self.set_mark(r, c, ship_letter)
                except CellError as err_msg:
                    print(err_msg)

    def get_ship(self, row: int, col: int) -> "Ship":
        mark = self.get_mark(row, col)
        for ship in self.ships:
            ship_letter = ship.name[0]
            if mark == ship_letter:
                return ship
        return None

    def damaged_cell_count(self, ship: Ship, scanning_board: Board) -> int:
        damaged_count = 0
        ship_placement = self.ship_placements[ship]
        for r in range(ship_placement.row_start, ship_placement.row_end + 1):
            for c in range(ship_placement.col_start, ship_placement.col_end + 1):
                if scanning_board.get_mark(r, c) == 'X':
                    damaged_count += 1
        return damaged_count

    def ship_destroyed(self, ship: Ship, scanning_board: Board):
        damaged_count = self.damaged_cell_count(ship, scanning_board)
        return damaged_count == ship.length


