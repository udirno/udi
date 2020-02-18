from typing import Iterable
from src.ship import Ship
from src.orientation import Orientation
from src.board import Board, ShipBoard
from src.move import Move
from src.players.player import Player
import random

class AiPlayer(Player):
    def __init__(self, num : int, all_players: Iterable["Player"],
                 ships_ : Iterable["Ship"], num_rows_ : int, num_cols_ : int,
                 blank_char_: str) -> None:
        super().__init__(num, all_players, ships_, num_rows_, num_cols_, blank_char_)

    def get_name_from_player(self, other_players: Iterable["Player"]) -> str:
        possible_names = ['Bob', 'Sally', 'Laura', 'Mike']
        other_player_names = [player.name for player in other_players]
        while True:
            name = random.choice(possible_names)
            if name not in other_player_names:
                return name

    def get_ship_orientation(self, ship_: Ship) -> Orientation:
        return random.choice([Orientation.HORIZONTAL, Orientation.VERTICAL])

    def get_ship_start_coords(self, ship_: Ship, orientation_: Orientation):
        if orientation_ == Orientation.HORIZONTAL:
            row = random.randint(0, self.ship_board.num_rows - 1)
            col = random.randint(0, self.ship_board.num_cols - ship_.length)
        else:
            row = random.randint(0, self.ship_board.num_rows - ship_.length)
            col = random.randint(0, self.ship_board.num_cols - 1)
        return row, col

    def get_move(self, the_board: "board.Board") -> "move.Move":
        empty_coordinates = the_board.get_empty_coordinates()
        coord = random.choice(empty_coordinates)
        return move.Move(self, *coord)

