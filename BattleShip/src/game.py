from typing import Iterable, Type, TypeVar
from src.ship import Ship
from src.board import Board
from src.players.human_player import HumanPlayer
from src.players.ais.random_ai import RandomAi
from src.players.ais.search_destroy_ai import SearchDestroyAi
from src.players.ais.cheating_ai import CheatingAi

T = TypeVar('T')

class Game(object):
    def __init__(self, ship_args: {str, int}, num_rows_: int, num_cols_: int, blank_char_: str = '*') -> None:
        self.blank_char = blank_char_
        self.ships = []
        for ship_name, ship_size in ship_args.items():
            self.ships.append(Ship(ship_name, ship_size))

        self.players = []
        for player_num in range(2):
            player_type = self.pick_player_type()
            self.players.append(player_type(player_num, self.players, self.ships,
                                       num_rows_, num_cols_, blank_char_))
        self._cur_player_turn = 0

    def pick_player_type(self) -> Type:
        possible_players = {
            'Human': HumanPlayer,
            'CheatingAi': CheatingAi,
            'SearchDestroyAi': SearchDestroyAi,
            'RandomAi': RandomAi
        }

        while True:
            picked_type = input(f'Enter one of {list(possible_players)} for your type: ').strip()
            for name, type in possible_players.items():
                # picked_type is a prefix of name if name startswith picked_type
                if name.startswith(picked_type):
                    return type
            else:
                print(f'{picked_type} is not one of {list(possible_players)}')


    def play(self) -> None:
        while not self.is_game_over():
            self.display_game_state()
            self.cur_player.take_turn(self.other_player())
            self.display_game_state()
            self.change_turn()

        # because we always change turns after a player wins
        # it will actually be the losing player's "turn"
        # and so we have to change turns one more time
        # so the correct player is declared the winner
        self.change_turn()
        self.display_game_state()
        self.display_the_winner()

    def merge_boards(self, ship_board, scan_board) -> "Board":
        merged_board = ship_board
        for r in range(len(merged_board.contents)):
            for c in range(len(merged_board.contents[0])):
                scan_char = scan_board[r][c]
                if scan_char != self.blank_char:
                    merged_board[r][c] = scan_char
        return merged_board

    # def display_game_state(self) -> None:
    #     print(f'{self.cur_player.name}\'s Scanning Board\n {self.cur_player.scanning_board}' + '\n')
    #     print(f'{self.cur_player.name}\'s Board\n {self.cur_player.ship_board}' + '\n')

    #def merge_board(self) -> None:
    def display_game_state(self) -> None:
        print(f'{self.cur_player.name}\'s Scanning Board\n {self.cur_player.scanning_board}' + '\n')
        merged_board = self.merge_boards(self.cur_player.ship_board, self.other_player().scanning_board)
        print(f'{self.cur_player.name}\'s Board\n {merged_board}' + '\n')

    def display_the_winner(self) -> None:
        print(f'{self.cur_player.name} won the game!')

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

    @property
    def cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]

    def other_player(self) -> "Player":
        other_player_turn = (self._cur_player_turn + 1) % 2
        return self.players[other_player_turn]

    def is_game_over(self) -> bool:
        result = True
        opponent = self.other_player()
        for ship in self.ships:
            if not self.cur_player.ship_board.ship_destroyed(ship, opponent.scanning_board):
                result = False
                break
        return result



        #return self.someone_won() or self.tie_game()

    def someone_won(self) -> bool:
        # TODO
        return False

    def tie_game(self) -> bool:
        # TODO
        return False


'''

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

    def display_the_winner(self):
        if self.someone_won():
            print(f'{self.cur_player} won the game!')
        else:
            print('Tie Game.')
'''
