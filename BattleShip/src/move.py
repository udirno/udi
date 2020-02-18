from src.board import Board, ShipBoard

class MoveError(Exception):
    ...

class Move(object):
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    @classmethod
    def from_str(cls, str_move: str) -> "Move":
        """
        :param maker:
        :param str_move: should be in the form row, col
        :return:
        """
        try:
            row, col = str_move.split(',')
        except ValueError:
            raise MoveError(f'{str_move} is not in the form row, col')

        try:
            row = int(row)
        except ValueError:
            raise MoveError(f'row needs to be an integer. {row} is not an integer')

        try:
            col = int(col)
        except ValueError:
            raise MoveError(f'col needs to be an integer. {col} is not an integer')

        return cls(row, col)

    def make(self, scan_board: Board, opponent_name: str, opponent_board: ShipBoard) -> str :
        if not scan_board.is_in_bounds(self.row, self.col):
            raise MoveError(f'{self.row}, {self.col} is not in bounds')
        elif not scan_board.is_blank(self.row, self.col):
            raise MoveError(f"You can't play at {self.row}, {self.col} because someone already played there")
        else:
            opponent_ship = opponent_board.get_ship(self.row, self.col)
            new_mark = 'O' if opponent_ship == None else 'X'
            scan_board.set_mark(self.row, self.col, new_mark, False)
            if opponent_ship == None:
                score_msg = print_msg = 'Miss.'
            elif opponent_board.damaged_cell_count(opponent_ship, scan_board) == opponent_ship.length:
                print(f'You hit {opponent_name}\'s {opponent_ship.name}' + '!')
                print_msg = f'You destroyed {opponent_name}\'s {opponent_ship.name}'
                score_msg = "Destroy"
            else:
                print_msg = f'You hit {opponent_name}\'s {opponent_ship.name}' + '!'
                score_msg = "Hit"
        print(print_msg)
        return score_msg