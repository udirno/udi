from typing import Iterator, List, Tuple
from .ship import Ship

class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str) -> None:
        #2d list of list
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
        # for row in self:
        #     for space in row:
        #         space != self.blank_char

    def is_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self.num_rows and
                0 <= col < self.num_cols)

    def get_ship_ends(self, ship: Ship, row: int, col: int, orientation: str) -> Tuple[int, int]:
        erow, ecol = row, col
        if orientation == 'horizontal':
            ecol = col+ship.size-1
        elif orientation == 'vertical':
            erow = row+ship.size-1
        return (erow, ecol)

    def ship_cells(self, ship: Ship, row: int, col: int, orientation: str) :
        erow, ecol = self.get_ship_ends(ship, row, col, orientation)
        gen_exp = (((r, c) for c in range(col, ecols+1)) for r in range(row, erows+1))
        return gen_exp

    def can_place(self, ship: "Ship", row: int, col: int, orientation: str) -> bool:
        #go through each cell the ship is on, check if it is on the board and if it is a blank character
        result = True
        erow, ecol = self.get_ship_ends(ship, row, col, orientation)
        for r in range(row, erow+1):
            for c in range(col, ecol+1):
                if not self.is_in_bounds(r, c):
                    result = False
                    break
                elif self.contents[r][c] != self.blank_char:
                    result = False
                    break
            if not result:
                break
        return result

    # very similar to can_place - loop over all cell and mark them
    def place(self, ship: "Ship", row: int, col: int, orientation: str) -> None:
        if not self.can_place(ship, row, col, orientation):
            return
        erow, ecol = self.get_ship_ends(ship, row, col, orientation)
        ship_letter = ship.name[0]
        for r in range(row, erow+1):
            for c in range(col, ecol+1):
                self.contents[r][c] = ship_letter

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
