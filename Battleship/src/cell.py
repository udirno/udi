class CellError(Exception):
    def __init__(self, message):
        print(f'CellError: {message}')

class Cell(object):
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    ''' Construct a Cell from a string which should be in the form row, col. Since Python 
    classes can't have multiple constructors, use a class method and constructs a Cell inside 
    that method.  
    '''
    @classmethod
    def from_str(cls, str_cell: str) -> "Cell":
        try:
            row, col = str_cell.split(',')
        except ValueError:
            raise CellError(f'{str_cell} is not in the form row, col')
        try:
            row = int(row)
        except ValueError:
            raise CellError(f'row needs to be an integer. {row} is not an integer')
        try:
            col = int(col)
        except ValueError:
            raise CellError(f'col needs to be an integer. {col} is not an integer')
        return cls(row, col)
