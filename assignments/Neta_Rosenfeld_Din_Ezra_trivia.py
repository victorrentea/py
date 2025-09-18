from random import randrange

class Player:
    def __init__(self, name):
        self.name = name
        self.place = 0
        self.purse = 0
        self.in_penalty_box = False
        self.is_getting_out_of_penalty_box = False       


class Game:
    def __init__(self):
        """Initializes the game with no players and sets up the game board."""
        self.players = []
        self.current_player = 0

        self.category_map = {
            0: 'Pop', 4: 'Pop', 8: 'Pop',
            1: 'Science', 5: 'Science', 9: 'Science',
            2: 'Sports', 6: 'Sports', 10: 'Sports'
        }

        self.questions_map = {
            'Pop': self.create_questions('Pop', 50),
            'Science': self.create_questions('Science', 50)  ,
            'Sports': self.create_questions('Sports', 50),
            'Rock': self.create_questions('Rock', 50),
        }

            
    @staticmethod
    def create_questions(category_name, n_questions):
        """Creates a list of questions for a given category."""
        questions = []
        for i in range(n_questions):
            questions.append(f"{category_name} Question {i}")
        return questions

    def is_playable(self):
        """Checks if the game can be played."""
        return self.how_many_players >= 2

    def add(self, player_name: str):
        """Adds a player to the game.
        Raises ValueError if player already exists or TypeError if player_name is not a string. """ 

        if type(player_name )!= str:
            raise TypeError("Player name must be a string")
        if player_name in [player.name for player in self.players]:
            raise ValueError("Player already exists")
            
        player = Player(player_name)
        self.players.append(player)
        print(f"{player_name} was added")
        print(f"They are player number {len(self.players)}")
     

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll: int):
        """Simulates rolling a die and moving the current player. """    
        player = self.players[self.current_player]
        print("%s is the current player" % player.name)
        print("They have rolled a %s" % roll)

        if player.in_penalty_box:
            if roll % 2 != 0:
                player.is_getting_out_of_penalty_box = True
                print("%s is getting out of the penalty box" % player.name)

                player.place = (player.place + roll) % 12
                print(f"{player.name}'s new location is {player.place}")
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % player.name)
                player.is_getting_out_of_penalty_box = False
        else:
            player.place = (player.place + roll) % 12
            print(f"{player.name}'s new location is {player.place}")
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        """Ask and remove the next question from the current category."""
        print(self.questions_map[self._current_category].pop(0))

    @property
    def _current_category(self):
        """Returns the current category based on the player's position."""
        return self.category_map.get(self.players[self.current_player].place, 'Rock')

    def _next_player(self):
        """Moves to the next player."""
        self.current_player = (self.current_player + 1) % len(self.players)

    def was_correctly_answered(self)->bool:
        """Handles the case when a player answers correctly."""
        player = self.players[self.current_player]
        if player.in_penalty_box and not player.is_getting_out_of_penalty_box:
            self._next_player()
            return False

        print('Answer was correct!!!!')
        player.purse += 1
        print(f'{player.name} now has {player.purse} gold Coins.')

        is_winner:bool = self._did_player_win()
        self._next_player()
        return is_winner


    def wrong_answer(self):
        """"Handles the case when a player answers incorrectly."""
        print('Question was incorrectly answered')
        print(self.players[self.current_player].name + " was sent to the penalty box")
        self.players[self.current_player].in_penalty_box = True

        self._next_player()

    def _did_player_win(self):
        return (self.players[self.current_player].purse == 6)


if __name__ == '__main__':
    a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        # randomly decide if the answer is correct with p=0.(1)
        if randrange(9) == 7:
            game.wrong_answer()
        else:
            a_winner = game.was_correctly_answered()

        if a_winner: break