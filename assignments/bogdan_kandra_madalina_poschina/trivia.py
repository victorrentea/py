#!/usr/bin/env python3
from random import randrange


class Game:
    def __init__(self, winning_score=6, board_size=12):
        self.winning_score = winning_score
        self.board_size = board_size
        self.players = []
        self.places = []
        self.purses = []
        self.in_penalty_box = []
        self.winner = False

        self.questions = {
            "Pop": [f"Pop Question {i}" for i in range(50)],
            "Science": [f"Science Question {i}" for i in range(50)],
            "Sports": [f"Sports Question {i}" for i in range(50)],
            "Rock": [f"Rock Question {i}" for i in range(50)]
        }

        self.category_order = {
            0: "Pop",
            1: "Science",
            2: "Sports",
            3: "Rock",
            4: "Pop",
            5: "Science",
            6: "Sports",
            7: "Rock",
            8: "Pop",
            9: "Science",
            10: "Sports",
            11: "Rock"
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
        return self.category_order.get(
            self.places[self.current_player],
            "Rock"
            )

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
