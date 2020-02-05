import copy
from typing import Iterator, List, Tuple
from .ship import Ship
from .cell import Cell, CellError

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
    def is_in_bounds(self, cell: "Cell") -> bool:
        return (0 <= cell.row < self.num_rows and
                0 <= cell.col < self.num_cols)

    def available(self, cell: "Cell") -> bool:
        return self.is_in_bounds(cell) and \
            self.contents[cell.row][cell.col] == self.blank_char

    '''
    Place a piece in the cell if it is not occupied or out of bounds; otherwise raise CellError.
    '''
    def occupy(self, cell: "Cell", piece: str):
        if not self.is_in_bounds(cell):
            raise CellError(f'{cell.row}, {cell.col} is not in bounds')
        elif self.contents[cell.row][cell.col] != self.blank_char:
            raise CellError(f"location {cell.row}, {cell.col} is already occupied")
        else:
            self.contents[cell.row][cell.col] = piece

    def get_ship_end(self, ship: "Ship", scell: "Cell", orientation: str) -> "Cell":
        ecell = copy.copy(scell)
        if orientation == 'horizontal':
            ecell.col = scell.col+ship.size-1
        elif orientation == 'vertical':
            ecell.row = scell.row+ship.size-1
        return ecell

    def cells(self, ship: "Ship", scell: "Cell", orientation: str) :
        gen_exp = (Cell(r, c) for c in range(len(self.contents)) for r in range(self.contents[0]))
        return gen_exp

    def ship_cells(self, ship: "Ship", scell: "Cell", orientation: str) :
        ecell = self.get_ship_end(ship, scell, orientation)
        gen_exp = ((Cell(r, c) for c in range(scell.col, ecell.col+1)) for r in range(scell.ros, ecell.row+1))
        return gen_exp

    ''' Check if placing ship at row, col with orientation is valid, i.e each cell
        the ship is on, the board and the cell is empty, i.e. contains a blank
        character '''
    def ship_fits(self, ship: "Ship", scell: "Cell", orientation: str) -> bool:
        result = True
        ecell = self.get_ship_end(ship, scell, orientation)
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
        ecell = self.get_ship_end(ship, scell, orientation)
        print(f'placing {ship.name} from {scell.row}, {scell.col} to {ecell.row}, {ecell.col}')
        for r in range(scell.row, ecell.row+1):
            for c in range(scell.col, ecell.col+1):
                self.occupy(Cell(r, c), ship_letter)

'''
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