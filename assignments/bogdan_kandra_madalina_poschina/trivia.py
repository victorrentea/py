#!/usr/bin/env python3
from enum import Enum
from random import randrange
import string

class Subject(Enum):
    POP = "Pop"
    SCIENCE = "Science"
    SPORTS = "Sports"
    ROCK = "Rock"


class Game:
    def __init__(self, winning_score=6, board_size=12):
        self.winning_score = winning_score
        self.board_size = board_size
        self.players = []
        self.places = []
        self.purses = []
        self.in_penalty_box = []
        self.winner = False

        self.questions:dict[Subject,list(str)] = { # type: ignore
            Subject.POP: [f"Pop Question {i}" for i in range(50)],
            Subject.SCIENCE: [f"Science Question {i}" for i in range(50)],
            Subject.SPORTS: [f"Sports Question {i}" for i in range(50)],
            Subject.ROCK: [f"Rock Question {i}" for i in range(50)]
        }

        self.category_order = {
            0: Subject.POP,
            1: Subject.SCIENCE,
            2: Subject.SPORTS,
            3: Subject.ROCK,
            4: Subject.POP,
            5: Subject.SCIENCE,
            6: Subject.SPORTS,
            7: Subject.ROCK,
            8: Subject.POP,
            9: Subject.SCIENCE,
            10: Subject.SPORTS,
            11: Subject.ROCK
        }

        self.current_player = 0

    def add(self, player_name):
        self.players.append(player_name)
        self.places.append(0)
        self.purses.append(0)
        self.in_penalty_box.append(False)

        print(f"{player_name} was added")
        print(f"They are player number {len(self.players)}")

    def roll(self, roll):
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                print(f"{self.players[self.current_player]} is getting out of the penalty box")
                self.in_penalty_box[self.current_player] = False
            else:
                print(f"{self.players[self.current_player]} is not getting out of the penalty box")
                self.in_penalty_box[self.current_player] = True

        if not self.in_penalty_box[self.current_player]:
            self.places[self.current_player] = (self.places[self.current_player] + roll) % 12
            print(f"{self.players[self.current_player]}'s new location is {str(self.places[self.current_player])}")
            print(f"The category is {self._current_category()}")
            self._ask_question()

    def _ask_question(self):
        print(self.questions[self._current_category()].pop(0))

    def _current_category(self):
        return self.category_order.get(self.places[self.current_player],"Rock")

    def _next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)
    
    def correct_answer(self):
        if self.in_penalty_box[self.current_player]:
            self._next_player()
        else:
            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(f"{self.players[self.current_player]} now has {self.purses[self.current_player]} Gold Coins.")
            self.winner = self.purses[self.current_player] == self.winning_score
            self._next_player()

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(f"{self.players[self.current_player]} was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        self._next_player()


if __name__ == '__main__':
    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while not game.winner:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            game.wrong_answer()
        else:
            game.correct_answer()
