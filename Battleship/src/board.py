'''
left diagonal:
x
 x
  x

right diagonal:
  x
 x
x
return all_same((self.board[i][i] for i in range (self.board.num_rows))) #this is a generator expression
'''
# Two ways of picking up every other element of a list
# e.g. produce [1, 5, 9] from [1, 3, 5, 7, 9]
#iterable = [1, 3, 5, 7, 9]

# Alternative 1. Track position with an explicit index counter
from typing import Iterator, List

class Board(object):
    def __init__(self, num_rows: int, num_cols: int, blank_char: str) -> None:
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

    def get_ship_ends(ship: Ship, row: int, col: int, orientation: str) -> Tuple:
        erow, ecol = row, col
        if orientation == 'horizontal':
            ecol = col-ship.size+1
        elif orientation == 'vertical':
            erow = row-ship.size+1
        return (erow, ecol)

    def can_place(self, ship: Ship, row: int, col: int, orientation: str) -> bool:
        result = self.is_in_bounds(row, col)
        if result:
            erow, ecol = self.get_ship_ends(ship, row, col, orientation)
            result = self.is_in_bounds(erow, ecol)
        return result

    # Assume a valid placement exists - we will not check but just place
    def place(self, ship: Ship, row: int, col: int, orientation: str) -> None:
        if !self.can_place(Ship, row, col, orientation):
            return
        erow, ecol = get_ship_ends(ship, row, col, orientation)
        for r in range(row, erow+1):

        result = is_in_bounds(row, col)
        if result:
            erow, ecol = get_ship_ends(ship, row, col, orientation)
            resutl = is_in_bounds(erow, ecol)
        return result

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
'''

b = Board(args to make a board)
for row in b:
  for spot in row:
    do something with spot


#to iterate through instance of board and not through board class
for row in board:
    for spot in row:
        do something with spot