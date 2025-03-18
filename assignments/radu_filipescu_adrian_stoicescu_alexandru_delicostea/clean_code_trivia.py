#!/usr/bin/env python3

MAX_PLAYER_NUMBER = 6
QUESTION_DECK_SIZE = 50

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * MAX_PLAYER_NUMBER
        self.purses = [0] * MAX_PLAYER_NUMBER
        self.in_penalty_box = [0] * MAX_PLAYER_NUMBER

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0

        for i in range(QUESTION_DECK_SIZE):
            self.pop_questions.append(self.create_question(i, 'Pop'))
            self.science_questions.append(self.create_question(i, 'Sciences'))
            self.sports_questions.append(self.create_question(i, 'Sports'))
            self.rock_questions.append(self.create_question(i, 'Rock'))

    def create_question(self, index, question_type):
        return f"{question_type} Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 == 0:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
            else:
                self.in_penalty_box[self.current_player] = False
                print("%s is getting out of the penalty box" % self.players[self.current_player])
                
        if self.in_penalty_box[self.current_player] == False:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        categories = ['Pop', 'Science', 'Sports', 'Rock']
        return categories[self.places[self.current_player] % 4]

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            self.current_player += 1
            if self.current_player == len(self.players): 
                self.current_player = 0

            return True
        else:
            print("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): 
                self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return self.purses[self.current_player] != 6


from random import randrange

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