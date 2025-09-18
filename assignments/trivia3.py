from random import randrange


# type Qu
class Game:
    def __init__(self):
        self.players = []  # Player furat
        self.places = []
        self.purses = []
        self.in_penalty_box = []

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append(f"Pop Question {i}")  # comprehensii
            self.science_questions.append(f"Science Question {i}")
            self.sports_questions.append(f"Sports Question {i}")
            self.rock_questions.append(f"Rock Question {i}")

    @property
    def no_players(self):
        return len(self.players)

    @property
    def _current_category(self):
        match self.places[self.current_player] % 4:
            case 0:
                return 'Pop'
            case 1:
                return 'Science'
            case 2:
                return 'Sports'
            case _:
                return 'Rock'

    def _ask_question(self):
        match self._current_category:
            case 'Pop':  # ENUM
                print(self.pop_questions.pop(0))
            case 'Science':
                print(self.science_questions.pop(0))
            case 'Sports':
                print(self.sports_questions.pop(0))
            case 'Rock':
                print(self.rock_questions.pop(0))

    def _increment_player(self):  # tech name
        self.current_player = (self.current_player + 1) % self.no_players

    def _did_player_win(self):
        return self.purses[self.current_player] == 6

    def add_player(self, player_name):
        self.players.append(player_name)
        self.places.append(0)
        self.purses.append(0)
        self.in_penalty_box.append(False)

        print(player_name + " was added")
        print(f"They are player number {self.no_players}")

    def roll_dice(self, roll):
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True
                print(f"{self.players[self.current_player]} is getting out of the penalty box")
            else:
                print(f"{self.players[self.current_player]} is not getting out of the penalty box")
                self.is_getting_out_of_penalty_box = False
                return

        self.places[self.current_player] = (self.places[self.current_player] + roll) % 12
        print(f"{self.players[self.current_player]}'s new location is {self.places[self.current_player]}")
        print(f"The category is {self._current_category}")

        self._ask_question()

    def correct_answer(self):
        if self.in_penalty_box[self.current_player] and not self.is_getting_out_of_penalty_box:
            self._increment_player()
            return False

        print("Answer was correct!!!!")
        self.purses[self.current_player] += 1
        print(f"{self.players[self.current_player]} now has {self.purses[self.current_player]} Gold Coins.")

        is_winner = self._did_player_win()
        self._increment_player()

        return is_winner

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(f"{self.players[self.current_player]} was sent to the penalty box")

        self.in_penalty_box[self.current_player] = True
        self._increment_player()

        return False


if __name__ == '__main__':
    is_winner = False
    game = Game()

    game.add_player('Chet')
    game.add_player('Pat')
    game.add_player('Sue')

    while True:
        game.roll_dice(randrange(5) + 1)

        if randrange(9) == 7:
            is_winner = game.wrong_answer()
        else:
            is_winner = game.correct_answer()

        if is_winner:
            break
