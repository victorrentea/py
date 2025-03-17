#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players = []
        self.places = []
        self.purses = []
        self.in_penalty_box = []
        self.current_player = 0
        self.coins_to_win = 6
        self.winner = False

        self.category_question_indexes = {"Pop": 0, "Science": 0, "Sports": 0, "Rock": 0}

        self.places_question_categories = {0: "Pop", 1: "Science", 2: "Sports", 3: "Rock", 
                                  4: "Pop", 5: "Science", 6: "Sports", 7: "Rock",
                                  8: "Pop", 9: "Science", 10: "Sports", 11: "Rock"}
        
    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places.append(0)
        self.purses.append(0)
        self.in_penalty_box.append(False)

        print(f"{player_name} was added")
        print(f"They are player number {self.how_many_players}")

    @property
    def how_many_players(self):
        return len(self.players)
    
    def update_place(self, roll):
        self.places[self.current_player] = (self.places[self.current_player] + roll) % 12

    def remains_in_penalty_box(self, roll):
        return self.in_penalty_box[self.current_player] and roll % 2 == 0    

    def roll(self, roll):
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")

        if self.remains_in_penalty_box(roll):
            print(f"{self.players[self.current_player]} is not getting out of the penalty box")
        else: 
            if self.in_penalty_box[self.current_player]:
                self.in_penalty_box[self.current_player] = False
                print(f"{self.players[self.current_player]} is getting out of the penalty box")

            self.update_place(roll)
            print(f"{self.players[self.current_player]}'s new location is {self.places[self.current_player]}")
            print(f"The category is {self._current_category}")
            self._ask_question()

    def _ask_question(self):
        print(f"{self._current_category} Question {self.category_question_indexes[self._current_category]}")
        self.category_question_indexes[self._current_category] +=1

    @property
    def _current_category(self):
        return self.places_question_categories[self.places[self.current_player]]
    
    def next_player(self):
        self.current_player = (self.current_player + 1) % self.how_many_players

    def correct_answer(self):
        if self.in_penalty_box[self.current_player]:
            self.next_player()
        else:
            print('Answer was correct!!!!')
            self.purses[self.current_player] += 1
            print(f'{self.players[self.current_player]} now has {self.purses[self.current_player]} Gold Coins.') 
            self.winner = self._did_player_win()
            self.next_player()

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(f"{self.players[self.current_player]} was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        self.next_player()

    def _did_player_win(self):
        return self.purses[self.current_player] == self.coins_to_win
    
from random import randrange

if __name__ == '__main__':
    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while game.is_playable:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            game.wrong_answer()
        else:
            game.correct_answer()

        if game.winner: break
