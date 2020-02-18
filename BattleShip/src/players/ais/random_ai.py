from typing import Iterable
from src.ship import Ship
from src.players.ais.ai_player import AiPlayer
from src.move import Move
import random


class RandomAi(AiPlayer):
    def __init__(self, num : int, all_players: Iterable["Player"],
                 ships_ : Iterable["Ship"], num_rows_ : int, num_cols_ : int,
                 blank_char_: str) -> None:
        super().__init__(num, all_players, ships_, num_rows_, num_cols_, blank_char_)
        self.firing_locations = self.scanning_board.get_empty_coordinates()

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        return super().get_name_with_prefix('Random AI', other_players)

    def get_move(self, opponent : "Player") -> Move:
        coord = random.choice(self.firing_locations)
        self.firing_locations.remove(coord)
        return Move(*coord)


