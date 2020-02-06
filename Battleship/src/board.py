from typing import Iterable, Iterator, List, Tuple
from .ship import Ship
from .cell import Cell, CellError

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
        rep = sep * 2 + sep.join((str(i) for i in range(self.num_cols))) + '\n'
        for row_index, row in enumerate(self):
            rep += str(row_index) + sep + sep.join(row) + '\n'
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

    def is_in_bounds(self, cell: "Cell") -> bool:
        return (0 <= cell.row < self.num_rows and
                0 <= cell.col < self.num_cols)
    def get_content(self, cell: "Cell"):
        if self.is_in_bounds(cell):
            return self.contents[cell.row][cell.col]

    def available(self, cell: "Cell") -> bool:
        return self.is_in_bounds(cell) and \
            self.get_content(cell) == self.blank_char

    '''
    Place a piece in the cell if it is not occupied or out of bounds; otherwise raise CellError.
    '''
    def set_content(self, cell: "Cell", mark: str, check_occupied = True):
        if not check_occupied:
            self.contents[cell.row][cell.col] = mark
        else:
            if not self.is_in_bounds(cell):
                raise CellError(f'{cell.row}, {cell.col} is not in bounds')
            elif self.get_content(cell) != self.blank_char:
                raise CellError(f"location {cell.row}, {cell.col} is already occupied")
            else:
                self.contents[cell.row][cell.col] = mark

''' ShipBoard is derived from Board. It is a board with ships on it. '''
class ShipBoard(Board):
    def __init__(self, num_rows: int, num_cols: int, ships: Iterable["Ship"], blank_char: str):
        super().__init__(num_rows, num_cols, blank_char)
        self.ships = ships
        self.ship_placements = []


    ''' Check if placing ship at row, col with orientation is valid, i.e each cell
        the ship is on, the board and the cell is empty, i.e. contains a blank
        character '''
    def ship_fits(self, ship: "Ship", scell: "Cell", orientation: str) -> bool:
        result = True
        ecell = ship.get_end_cell(scell, orientation)
        for r in range(scell.row, ecell.row+1):
            for c in range(scell.col, ecell.col+1):
                if not self.available(Cell(r, c)):
                    result = False
                    break
            if not result:
                break
        return result

    '''
    Loop over all cells covered by the ship and mark them with the first letter of the ship
    name. Raise CellError if any of those cells are out of bounds or already occupied.
    '''
    def place_ship(self, ship: "Ship", scell: "Cell", orientation: str) -> None:
        ship_letter = ship.name[0]
        ecell = ship.get_end_cell(scell, orientation)
        for r in range(scell.row, ecell.row+1):
            for c in range(scell.col, ecell.col+1):
                self.set_content(Cell(r, c), ship_letter)

    def get_ship(self, cell: "Cells") -> "Ship":
        mark = self.get_content(cell)
        for ship in self.ships:
            ship_letter = ship.name[0]
            if mark == ship_letter:
                return ship
        return None

    def intact_cell_count(self, ship: "Ship", scanning_board: "Board") -> int:
        intact_count = 0
        scell, orientation = self.ship_placements[self.ships.index(ship)]
        ecell = ship.get_end_cell(scell, orientation)
        for c in range(scell.col, ecell.col + 1):
            for r in range(scell.row, ecell.row + 1):
                cell = Cell(r, c)
                if scanning_board.get_content(cell) != 'X':
                    intact_count += 1
        return intact_count



