class CellError(Exception):
    pass

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
            raise CellError(f'Row should be an integer. {row} is NOT an integer')
        try:
            col = int(col)
        except ValueError:
            raise CellError(f'Column should to be an integer. {col} is NOT an integer')
        return cls(row, col) #returns object of class Cell


