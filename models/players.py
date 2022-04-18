from models.game import *

class Player():
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice


player_selection = []


def add_player_selection(player_plays):
    player_selection.append(player_plays)
    print(player_selection)