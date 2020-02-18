from typing import Iterable
from src.ship import Ship
from src.orientation import Orientation
from src.board import Board, ShipBoard
from src.move import Move
from src.players.player import Player
import random
from src.players.ais.ai_player import AiPlayer

class CheatingAi(AiPlayer):
    def __init__(self, num : int, all_players: Iterable["Player"],
                 ships_ : Iterable["Ship"], num_rows_ : int, num_cols_ : int,
                 blank_char_: str) -> None:
        super().__init__(num, all_players, ships_, num_rows_, num_cols_, blank_char_)

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        return super().get_name_with_prefix('Cheating Ai', other_players)

    def get_move(self, opponent: "Player") -> Move:
        if self.firing_locations is None:
            self.firing_locations = opponent.ship_board.get_ship_coordinates()
        coord = random.choice(self.firing_locations)
        self.firing_locations.remove(coord)
        return Move(*coord)
