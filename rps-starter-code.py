#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            moveIndex = moves.index(self.my_move)
            moveIndex += 1
            if moveIndex > 2:
                moveIndex = 0
            move = moves[moveIndex]
            return move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            moveText = input("Rock, paper, scissors? > ")
            if moveText in moves:
                break
        return moveText.lower()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print(f"** TIE **")
        elif beats(move1, move2):
            self.p1score += 1
            print(f"** PLAYER ONE WINS **")
        else:
            self.p2score += 1
            print(f"** PLAYER TWO WINS **")

        print(f"Score: Player One {self.p1score}, Player Two {self.p2score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print(f"SCORE:Player ONE {self.p1score} - Player TWO {self.p2score}")
        if self.p1score > self.p2score:
            print(f"Player ONE has won the game!")
        elif self.p1score < self.p2score:
            print(f"Player TWO has won the game!")
        elif self.p1score == self.p2score:
            print(f"The game ended with a TIE!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
