#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
from random import randint

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return moves[randint(0, 2)]


class HumanPlayer(Player):
    def move(self):
        self.current_move = input("Enter your move: ")
        while self.current_move not in moves:
            print("Enter valid move! i.e 'rock', 'paper', 'scissors'")
            self.current_move = input("Enter your move: ")
        return self.current_move


class ReflectPlayer(Player):
    def __init__(self):
        self.current_move = moves[randint(0, 2)]

    def move(self):
        return self.current_move

    def learn(self, my_move, their_move):
        self.current_move = their_move


class CounterPlayer(Player):
    def __init__(self):
        self.current_move = moves[randint(0, 2)]

    def move(self):
        return self.current_move

    def learn(self, my_move, their_move):
        if their_move == "rock":
            self.current_move = "paper"
        elif their_move == "paper":
            self.current_move = "scissors"
        elif their_move == "scissors":
            self.current_move = "rock"


class CyclePlayer(Player):
    def __init__(self):
        self.current_move = "rock"

    def move(self):
        return self.current_move

    def learn(self, my_move, their_move):
        if my_move == "rock":
            self.current_move = "paper"
        elif my_move == "paper":
            self.current_move = "scissors"
        elif my_move == "scissors":
            self.current_move = "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def winner(player_score1, player_score2, game):
    if player_score1 > player_score2:
        print(f"Player 1 has won the {game}!")
    elif player_score1 < player_score2:
        print(f"Player 2 has won the {game}!")
    else:
        print(f"The {game} has ended in draw!")


def score_board(score1, score2):
    print(f"\nPlayer 1 Score: {score1} Player 2 Score: {score2}")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}   Player 2: {move2}")
        # If player 1 beats player 2 increase score for player 1
        # and vice versa
        if beats(move1, move2):
            self.score1 += 1
        elif beats(move2, move1):
            self.score2 += 1

        score_board(self.score1, self.score2)
        winner(self.score1, self.score2, "round")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("-----------------------------")
        print("Game Start!")
        print("Round 1:")
        self.play_round()
        score_board(self.score1, self.score2)
        winner(self.score1, self.score2, "game")
        print("Game Over!")
        print("-----------------------------\n\n")

    def play_games(self):
        # Continues to ask the number of rounds user wants to play
        # until user gives a correct integer
        while True:
            try:
                rounds = int(input("How many rounds do you want to play? "))
                break
            except ValueError:
                print("Enter proper integer")

        print("-----------------------------")
        print("Game Start!")
        for round in range(rounds):
            print(f"\nRound {round + 1}:")
            self.play_round()
        score_board(self.score1, self.score2)
        winner(self.score1, self.score2, "game")
        print("Game Over, Thank you for play with us!")
        print("-----------------------------\n\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_games()
