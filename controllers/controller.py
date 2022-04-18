
from flask import Flask, url_for, render_template, request, redirect
from app import app
from models.game import *
from models.players import *


@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html', title='Home')

# @app.route('/lets_play',  methods=['GET', 'POST'])
# def lets_play():
#     if request.method == "POST":
        # player = request.form["name1"]
        # player1 = request.form['name1']
        # player1_choice = request.form['choice1']
        # player2 = request.form['name2']
        # player2_choice = request.form['choice2']
        # return player
        # rock_paper_scissors(player1, player1_choice, player2, player2_choice)
        # return redirect(url_for("player1_choice", choice1=player1_choice))
    # else:

    # if request.method == 'POST':
    #     choice = request.form['choice']
    #     return redirect('result', choice=choice)

        # return render_template('lets_play.html', title='Play')


@app.route('/lets_play',  methods=['GET', 'POST'])
def lets_play():
    if request.method == "POST":

        player1 = request.form['name1']
        player1_choice = request.form['choice1']
        player2 = request.form['name2']
        player2_choice = request.form['choice2']
        
        
        winner = player2

        if player1_choice == player2_choice:
            winner = "It's a tie, go again!"
        if player1_choice == "rock" and player2_choice == "scissors":
            winner = player1
        if player1_choice == "scissors" and player2_choice == "paper":
            winner = player1
        if player1_choice == "paper" and player2_choice == "rock":
            winner = player1
        
        if winner == player1:
            winning_weapong = player1_choice
            losing_weapon = player2_choice
        else: 
            winning_weapong = player2_choice
            losing_weapon = player1_choice

        # return redirect(url_for("winner", winner=winner))
        return winning_weapong + " beats " + losing_weapon + ". the winner is... " + winner +"! "
       
    else:



        return render_template('lets_play.html', title='Play')


# @app.route('/<choice>',  methods=['GET', 'POST'])
# def player1_choice(player1_choice):
#     if request.method == "POST":
#         return f"<h1> selected {player1_choice}"
        # player = request.form["name1"]
        # player2 = request.form['name2']
        # player2_choice = request.form['choice2']
        # return player
    # else:

    # if request.method == 'POST':
    #     choice = request.form['choice']
    #     return redirect('result', choice=choice)

        # return render_template('lets_play.html', title='Play')
    

# @app.route('/<winner>')
# def winner():
#     return render_template('lets_play.html', title='Play')