from typing import Iterable
from src.ship import Ship
from src.orientation import Orientation
from src.board import Board, ShipBoard
from src.move import Move
from src.players.player import Player
import random
from src.players.ais.ai_player import AiPlayer
import collections

class SearchDestroyAi(AiPlayer):
    def __init__(self, num : int, all_players: Iterable["Player"],
                 ships_ : Iterable["Ship"], num_rows_ : int, num_cols_ : int,
                 blank_char_: str) -> None:
        super().__init__(num, all_players, ships_, num_rows_, num_cols_, blank_char_)
        self.firing_locations = self.scanning_board.get_empty_coordinates()
        self.destroy_locations = collections.deque()
        self.mode = "search"

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        return super().get_name_with_prefix('Search Destroy AI', other_players)

    def get_move(self, opponent: "Player") -> Move:
        coord = None
        if self.mode == "search" or not self.destroy_locations:
            coord = random.choice(self.firing_locations)
        elif self.mode == "destroy":
            coord = self.destroy_locations.popleft()
        if coord not in self.firing_locations:
            print(f'mode = {self.mode}, coord = {coord}, firing locations = {self.firing_locations}')
        self.firing_locations.remove(coord)
        return None if coord is None else Move(*coord)

    def change_strategy(self, move : Move, score_msg : str):
        super().change_strategy(move, score_msg)
        if score_msg == 'Miss':
            return
        self.mode = "destroy"
        for offset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            row = move.row + offset[0]
            col = move.col + offset[1]
            if row >= 0 and col >= 0 and self.scanning_board.is_blank(row,col):
                self.destroy_locations.append((row, col))
