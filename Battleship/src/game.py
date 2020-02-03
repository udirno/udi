from typing import Iterable, TypeVar
from .board import Board
from .player import Player

T = TypeVar('T')


class Game(object):
    def __init__(self, ship_args : {str, int}, num_rows: int, num_cols: int) -> None:
        self.board = Board(num_rows, num_cols)
        self.ships = []
        for ship_name, ship_size in ship_args.items():
            self.ships.append(Ship(ship_name,ship_size))


#DO THE SAME FOR PLAYERS AS FOR SHIPS
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players))
        self._cur_player_turn = 0
'''
    def __init__(self, dimensions: int, blank_char: str = '*') -> None:
        self.blank_char = blank_char
        self.board = Board(dimensions, dimensions, blank_char)
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players, blank_char))
        self._cur_player_turn = 0

    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            self.cur_player.take_turn(self.board)
            self.change_turn()

        # because we always change turns after a player wins
        # it will actually be the losing player's "turn"
        # and so we have to change turns one more time
        #so the correct player is declared the winner
        self.change_turn()
        self.display_game_state()
        self.display_the_winner()

    def display_game_state(self) -> None:
        print(self.board)

    def is_game_over(self):
        return self.someone_won() or self.tie_game()

    def someone_won(self) -> bool:
        """

        :return:
        """
        return self.someone_won_horizontally() or self.someone_won_vertically() or self.someone_won_diagonally()

    def someone_won_horizontally(self) -> bool:
        for row in self.board:
            if row[0] != self.blank_char and self.all_same(row):
                return True

        return False

        # for i in range(self.board.rows):
        #     if self.board.row_all_same(self.board[i])
        #
        # do any of the rows
        # have all of the same characters
        return any(
            (self.all_same(row) for row in self.board)
        )

    # a b c
    # d e f
    # h i j

    def someone_won_vertically(self) -> bool:
        for col in zip(*self.board):
            if col[0] != self.blank_char and self.all_same(col):
                return True
        else:
            return False

    def someone_won_diagonally(self) -> bool:
        return self.someone_won_with_left_diagonal() or self.someone_won_with_right_diagonal()

    def someone_won_with_left_diagonal(self) -> bool:
        """
        Someone won like this
        X
          X
            X
        :return:
        """
        return self.board[0][0] != self.blank_char and self.all_same((self.board[i][i] for i in range(self.board.num_rows)))

    def someone_won_with_right_diagonal(self) -> bool:
        """
        Some won like
            X
          X
        X
        :return:
        """
        row_indices = range(self.board.num_rows)
        col_indices = reversed(range(self.board.num_cols))
        return self.board[0][-1] != self.blank_char and self.all_same(
            (self.board[row][col] for row, col in zip(row_indices, col_indices))
        )

    @staticmethod
    def all_same(values: Iterable[T]) -> bool:
        iterator = iter(values)
        first_value = None
        try:
            first_value = next(iterator)
        except StopIteration:  # the iterable was empty
            return True  # so all elements are the same
        else:
            return all(
                (value == first_value for value in iterator)
            )

    def tie_game(self) -> bool:
        """
        This should only be called after a check for a win is done
        :return:
        """
        return self.board.is_full()

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2
        # if self._cur_player_turn == 0:
        #     self._cur_player_turn = 1
        # else:
        #     self._cur_player_turn = 0

    @property
    def cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]

    def display_the_winner(self):
        if self.someone_won():
            print(f'{self.cur_player} won the game!')
        else:
            print('Tie Game.')
'''
