#!/usr/bin/env python3
from enum import Enum


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


class QuestionType(Enum):
    POP = "Pop"
    SCIENCE = "Science"
    SPORTS = "Sports"
    ROCK = "Rock"


class Game:
    def __init__(self):
        self.players: list[Player] = []
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.player_index = 0
        self.is_getting_out_of_penalty_box = False

        self.questions = {e: [f"{e.value} Question {i}" for i in range(50)] for e in QuestionType}

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(Player(player_name))
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.current_player.name)
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.player_index]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.current_player.name)
                player = self.current_player
                player.advance(roll)

                print(self.current_player.name + '\'s new location is ' + str(self.current_player.place))
                print("The category is %s" % self.current_category.value)
                self.ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.current_player.name)
                self.is_getting_out_of_penalty_box = False
        else:
            player = self.current_player
            player.advance(roll)

            print(self.current_player.name + '\'s new location is ' + str(self.current_player.place))
            print("The category is %s" % self.current_category.value)
            self.ask_question()

    @property
    def current_player(self):
        return self.players[self.player_index]

    def ask_question(self):
        print(self.questions[self.current_category].pop(0))

    @property
    def current_category(self) -> QuestionType:
        mod_to_type = {
            0: QuestionType.POP,
            1: QuestionType.SCIENCE,
            2: QuestionType.SPORTS,
            3: QuestionType.ROCK
        }
        return mod_to_type[(self.current_player.place % 4)]

    def was_correctly_answered(self):
        if self.in_penalty_box[self.player_index]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.player_index] += 1
                print(self.current_player.name + ' now has ' + str(
                    self.purses[self.player_index]) + ' Gold Coins.')

                winner = self.__did_player_win()
                self.next_player()

                return winner
            else:
                self.next_player()
                return True
        else:

            print("Answer was corrent!!!!")
            self.purses[self.player_index] += 1
            print(self.current_player.name + ' now has ' + str(
                self.purses[self.player_index]) + ' Gold Coins.')

            winner = self.__did_player_win()
            self.next_player()

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.current_player.name + " was sent to the penalty box")
        self.in_penalty_box[self.player_index] = True

        self.next_player()
        return True

    def next_player(self):
        self.player_index += 1
        if self.player_index == len(self.players):
            self.player_index = 0

    def __did_player_win(self):
        return self.purses[self.player_index] != 6
