#!/usr/bin/env python3
from dataclasses import dataclass
from random import randrange


@dataclass
class Player:
    name: str
    place: int = 0
    coins: int = 0
    in_penalty_box: bool = False
    is_getting_out: bool = True


class Game:
    def __init__(self):
        self.players = []
        self.categories = ["pop", "science", "sports", "rock"]
        self.questions = self.gather_questions(self.categories)
        self.current_player_idx = 0

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_idx]

    @property
    def current_category(self):
        if self.current_player.place in [0, 4, 8]:
            return self.categories[0]
        elif self.current_player.place in [1, 5, 9]:
            return self.categories[1]
        elif self.current_player.place in [2, 6, 10]:
            return self.categories[2]
        else:
            return self.categories[3]

    def gather_questions(self, categories: list[str], count: int = 50) -> dict[str, list[str]]:
        questions = {}
        for i in range(count):
            for category in categories:
                questions.setdefault(category, []).append(f"{category.capitalize()} Question {i}")

        return questions

    def add_player(self, name: str) -> None:
        self.players.append(Player(name))
        print(f"Player {name} was added")
        print(f"They are player number {len(self.players)}")

    def roll(self, roll: int) -> None:
        print(f"{self.current_player.name} is the current player")
        print(f"They have rolled a {roll}")

        if self.current_player.in_penalty_box:
            self.current_player.is_getting_out = roll % 2 != 0
            if not self.current_player.is_getting_out:
                print(f"{self.current_player.name} is not getting out of the penalty box")
                return
            else:
                print(f"{self.current_player.name} is getting out of the penalty box")

        self.current_player.place = (self.current_player.place + roll) % 12

        print(f"{self.current_player.name}'s new location is {self.current_player.place}")

    def next_question(self) -> str | None:
        print(f"The category is {self.current_category}")
        try:
            return self.questions[self.current_category].pop(0)
        except IndexError:
            print(f"No more questions for the {self.current_category} category")
            return None

    def check_answer(self, answer: int) -> Player | None:
        if answer == 7:
            self.handle_correct_answer()
        else:
            self.handle_incorrect_answer()

        winner = self.check_winner()

        self.current_player_idx += 1
        self.current_player_idx %= len(self.players)

        return winner

    def handle_correct_answer(self):
        if not self.current_player.is_getting_out:
            return

        print("Answer was correct!!!!")
        self.current_player.coins += 1
        print(f"{self.current_player.name} now has {self.current_player.coins} Gold Coins.")

    def handle_incorrect_answer(self):
        print("Question was incorrectly answered")
        print(f"{self.current_player.name} was sent to the penalty box")
        self.current_player.in_penalty_box = True

    def check_winner(self) -> Player | None:
        if self.current_player.coins == 6:
            return self.current_player

        return None


if __name__ == "__main__":
    game = Game()

    game.add_player("Chet")
    game.add_player("Pat")
    game.add_player("Sue")

    while True:

        game.roll(randrange(5) + 1)

        game.next_question()

        winner = game.check_answer(randrange(9))

        if winner:
            print(f"{winner.name} won the game!")
            break
