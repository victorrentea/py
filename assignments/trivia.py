#!/usr/bin/env python3
from random import randrange

QUESTIONS_PER_CATEGORY = 50

BOARD_SIZE = 12


class Player:
    def __init__(self, name):
        self.name = name
        self.place = 0
        self.coins = 0
        self.in_penalty_box = False

    def move(self, roll):
        self.place += roll
        self.place %= BOARD_SIZE
        print("%s's new location is %s" % (self.name, self.place))

    def add_coin(self):
        self.coins += 1
        print("%s now has %s Gold Coins." % (self.name, self.coins))

    def is_a_winner(self):
        return self.coins == 6


class QuestionCategory(Enum):
    POP = "Pop"
    SCIENCE = "Science"
    SPORTS = "Sports"
    ROCK = "Rock"


class Game:
    def __init__(self):
        self.players = []
        self.current_player_index = 0

        # self.questions = {
        #     QuestionCategory.POP: ["Pop Question %s" % i for i in range(QUESTIONS_PER_CATEGORY)],
        #     QuestionCategory.SCIENCE: ["Science Question %s" % i for i in range(QUESTIONS_PER_CATEGORY)],
        #     QuestionCategory.SPORTS: ["Sports Question %s" % i for i in range(QUESTIONS_PER_CATEGORY)],
        #     QuestionCategory.ROCK: ["Rock Question %s" % i for i in range(QUESTIONS_PER_CATEGORY)]
        # }

        # self.questions = {
        #     category: [f"{category} Question {i}" for i in range(QUESTIONS_PER_CATEGORY)]
        #     for category in QuestionCategory
        # }

        self.questions = {
            category: self.generate_questions(category)
            for category in QuestionCategory
        }

    def generate_questions(self, category) -> list[str]:
        return [f"{category} Question {i}" for i in range(QUESTIONS_PER_CATEGORY)]

    def add(self, player_name):
        self.players.append(Player(player_name))
        if not self.current_player:
            self.current_player = self.players[0]

        print(f"{player_name} was added")
        print(f'Player number {self.how_many_players}')

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("\n%s is the current player" % self.current_player.name)
        print("They have rolled a %s" % roll)

        if self.current_player.in_penalty_box:
            if roll % 2 != 0:
                self.current_player.in_penalty_box = False
                print("%s is getting out of the penalty box" % self.current_player.name)
            else:
                print("%s is not getting out of the penalty box" % self.current_player.name)
                return

        self.current_player.move(roll)
        print("The category is %s" % self.current_category)
        self.ask_question()

    def ask_question(self):
        print(self.questions[self.current_category].pop(0))

    @property  # must be PURE
    def current_category(self) -> QuestionCategory:
        index = self.current_player.place % len(QuestionCategory)
        # if (index == 0): return QuestionCategory.POP
        # elif (index == 1): return QuestionCategory.SCIENCE
        # elif (index == 2): return QuestionCategory.SPORTS
        # else: return QuestionCategory.ROCK
        return list(QuestionCategory)[index]

    @property
    def current_player(self):
        return self.players[self.current_player_index]

    def update_current_player(self):
        self.current_player_index += 1
        self.current_player_index %= self.how_many_players

    def was_correctly_answered(self):
        not_a_winner = True
        if not self.current_player.in_penalty_box:
            print("Answer was corrent!!!!")
            self.current_player.add_coin()
            not_a_winner = not self.current_player.is_a_winner()

        self.update_current_player()
        return not_a_winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.current_player.name + " was sent to the penalty box")
        self.current_player.in_penalty_box = True

        self.update_current_player()
        return True


if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
