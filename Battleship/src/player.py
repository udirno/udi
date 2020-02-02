from typing import Iterable
from .move import Move, MoveError
from .board import Board

class Player(object):
    def __init__(self, players: Iterable["Player"], blank_character: str) -> None:
        self.name = self.player_names(players)
        self.piece = self.get_piece_from_player(other_players, blank_character)



def player_names(players: Iterable["Player"]) -> str:):
        while(True):
            p1_name = input("Enter Player one name:")
            p2_name = input("Enter Plater two name:")
            if p1_name == p2_name or p1_name == '' or p2_name == '':
                print('Please enter a different name:')
            else:
                return p1_name, p2_name
                break
