#!/usr/bin/env python3
class Player:
    def __init__(self, name):
        self.name = name
        self.gold_coins = 0
        self.in_penalty_box = False
        self.place = 0

    def advance(self, roll: int):
        self.place = self.place + roll
        if self.place > 11:
            self.place = self.place - 12


class Game:
    def __init__(self):
        self.players: list[Player] = []
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player_index = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(Player(player_name))
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player_index].name)
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player_index]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player_index].name)
                player = self.current_player()
                player.advance(roll)

                print(self.current_player().name + '\'s new location is ' + str(self.players[self.current_player_index].place))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player_index].name)
                self.is_getting_out_of_penalty_box = False
        else:
            player = self.current_player()
            player.advance(roll)

            print(self.players[self.current_player_index].name + \
                  '\'s new location is ' + \
                  str(self.players[self.current_player_index].place))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def current_player(self):
        return self.players[self.current_player_index]

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.players[self.current_player_index].place == 0: return 'Pop'
        if self.players[self.current_player_index].place == 4: return 'Pop'
        if self.players[self.current_player_index].place == 8: return 'Pop'
        if self.players[self.current_player_index].place == 1: return 'Science'
        if self.players[self.current_player_index].place == 5: return 'Science'
        if self.players[self.current_player_index].place == 9: return 'Science'
        if self.players[self.current_player_index].place == 2: return 'Sports'
        if self.players[self.current_player_index].place == 6: return 'Sports'
        if self.players[self.current_player_index].place == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player_index]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player_index] += 1
                print(self.players[self.current_player_index].name + ' now has ' + str(
                    self.purses[self.current_player_index]) + ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player_index += 1
                if self.current_player_index == len(self.players): self.current_player_index = 0

                return winner
            else:
                self.current_player_index += 1
                if self.current_player_index == len(self.players): self.current_player_index = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player_index] += 1
            print(self.players[self.current_player_index].name + ' now has ' + str(
                self.purses[self.current_player_index]) + ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player_index += 1
            if self.current_player_index == len(self.players): self.current_player_index = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player_index].name + " was sent to the penalty box")
        self.in_penalty_box[self.current_player_index] = True

        self.current_player_index += 1
        if self.current_player_index == len(self.players): self.current_player_index = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player_index] == 6)
