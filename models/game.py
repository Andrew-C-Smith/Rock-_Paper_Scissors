# from models.players import *

class Game():

    def __init__(self, player1_name, player1_choice, player2_name, player2_choice):
        self.player1_name = player1_name
        self.player1_choice = player1_choice
        self.player2_name = player2_name
        self.player2_choice = player2_choice


def rock_paper_scissors(player1_name, player1_selection, player2_selection, player2_name):
    player1_name = player1_name
    player2_name = player2_name

    if player1_selection == player2_selection:
        print("Its' a tie! We go Again!")
    elif player1_selection == "rock":
        if player2_selection == "scissors":
            print("Rock beat scissors, " )
        else:
            print("Paper covers rock! " )
    elif player1_selection == "paper":
        if player2_selection == "rock":
            print("Paper covers rock! " )
        else:
            print("Scissors cuts paper! " )
    elif player1_selection == "scissors":
        if player2_selection == "paper":
            print("Scissors cuts paper! " )
        else:
            print("Rock beats scissors! " )

rock_paper_scissors("andrew", "rock", "bill", "paper")