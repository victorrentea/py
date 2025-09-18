from collections import defaultdict
from random import randrange, seed
from typing import List
import logging
import argparse
from enum import Enum


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# custom decorators that make sense
# @retryable(3)
# @logged("prefix")
# @timed("metric_name")

# @service_method
# @lru_cache
# @dataclass
# @staticmethod
# @pytest.mark.serial
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         logger.info(f"Before {args}")
#         func(*args, **kwargs)
#         logger.info(f"After")
#
#     return wrapper


TRIVIA_CATEGORIES = ["Pop", "Science", "Sports", "Rock"]

class Category(Enum): # from v 3.4
    POP = "Pop"
    SCIENCE = "Science"
    SPORTS = "Sports"
    ROCK = "Rock"

NUM_COINS_TO_WIN = 6

NUM_LOCATION_SPOTS = 12

@dataclass(frozen=True)
class InteractionId:
    guid: str
# or IBAN, SWIFTCode, SSN, ClientId, OperatorId

class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self._location = 0
        self.coins = 0
        self.in_penalty_box = False

    def roll_a_die(self) -> int:
        """
        Returns:
            int: A random number between 1 and 6, inclusive.
        """

        return randrange(1, 7)

    @property
    def location(self):
        return self._location

    def move(self, roll: int) -> None:
        self._location = (self._location + roll) % NUM_LOCATION_SPOTS

    def is_winner(self) -> bool:
        return self.coins == NUM_COINS_TO_WIN


class Game:
    """
    This class manages the game state, players, questions, and game logic."""

    def __init__(self):
        self.players: List[Player] = []
        self.category_question_count = defaultdict(int)
        self.current_player: Player = None

    @property # this fakes a property via a method
    def player_count(self) -> int:
        return len(self.players)
    
    @property
    def is_playable(self) -> bool:
        return self.player_count >= 2
    
    @property
    def _current_category(self) -> Category:
        category_index = self.current_player.location % len(Category)
        return TRIVIA_CATEGORIES[category_index]
    
    def _ask_question(self) -> None:
        logger.info(f"{self._current_category} Question {self.category_question_count[self._current_category]}")
        self.category_question_count[self._current_category] += 1

    def _handle_wrong_answer(self) -> None:
        """
        Handles the logic for determining the outcome when a player answers incorrectly.
        Incorrect answers result in the player being sent to the penalty box.
        """

        logger.info("Question was incorrectly answered.")
        logger.info(f"{self.current_player.name} was sent to the penalty box.")

        self.current_player.in_penalty_box = True

    def _handle_right_answer(self) -> None:
        logger.info("Answer was correct!!!!")
        self.current_player.coins += 1
        logger.info(f"{self.current_player.name} now has {str(self.current_player.coins)} Gold Coins.")

    # close turn
    # end turn
    # finalize turn
    def _assign_next_player(self):
        self.current_player = self.players[(self.current_player.id + 1) % self.player_count]

    def add_player(self, player_name: str) -> None:
        """
        Adds a new player to the game. No duplicate or blank player names are allowed.
        Args:
            player_name (str): The name of the player to be added.
        """

        if not player_name:
            logger.error("Attempted to add player with an empty name.")
            raise ValueError("Player name cannot be empty")
        if any(player_name == p.name for p in self.players):
            logger.error("Attempted to add a player with a duplicate name.")
            raise ValueError(f"Player '{player_name}' already exists")

        new_player = Player(player_name, self.player_count)
        logger.info(f"{new_player.name} was added")
        logger.info(f"They are player number {new_player.id + 1}")
        self.players.append(new_player)
        if self.current_player is None:
            self.current_player = new_player

    def play_turn(self) -> bool:
        """
        This function determines the player's movement on the board based on the dice roll,
        checks if the player is in the penalty box, and decides whether they can leave the
        penalty box. It also updates the player's position, announces their new location,
        and asks a question based on the current category and determines whether a win state is achieved.

        Returns:
            bool: True if the game continues, False if the player has won and play should stop.
        """

        roll = self.current_player.roll_a_die()
        self.current_player.extra_prop = 1 #anathema - never ducktape one more attr to an instance of an existing class
        logger.info(f"{self.current_player.name} is the current player.")
        logger.info(f"They have rolled a {roll}")

        if not self.current_player.in_penalty_box or roll % 2 != 0:
            if roll % 2 != 0 and self.current_player.in_penalty_box:
                self.current_player.in_penalty_box = False
                logger.info(f"{self.current_player.name} is getting out of the penalty box")

            self.current_player.move(roll)
            logger.info(f"{self.current_player.name}'s new location is {str(self.current_player.location)}")
            logger.info(f"The category is {self._current_category}")
            self._ask_question()
        else:
            logger.info(f"{self.current_player.name} is not getting out of the penalty box")

        # probability  = 1/9
        is_wrong_answer = randrange(9) == 0
        if is_wrong_answer:
            self._handle_wrong_answer()
        elif not self.current_player.in_penalty_box:
            self._handle_right_answer()

        player_won = self.current_player.is_winner()
        
        if not player_won:
            self._assign_next_player()
            return True
        else:
            return False


def play_game(game: Game):
    while game.play_turn():
        pass


def main(players: List = ["Chet", "Pat", "Sue"], seed_number: int = 42):
    """
    Wrapper function to add players and play trivia game.
    Args:
        players (List): A list of player names to add: Default ["Chet", "Pat", "Sue"]
        seed_number (int): Seed for random number generator. Default: 42
    """
    seed(seed_number)

    game = Game()

    for player in players:
        game.add_player(player)

    if game.is_playable:
        play_game(game)
    else:
        logger.fatal(f"Not enough players to play the game, there are {game.player_count} players but at least 2 are required.")


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description = "Trivia Game")

    # Add arguments
    parser.add_argument("--players", 
                        type = str, 
                        default = ["Chet", "Pat", "Sue"], 
                        nargs = "+", 
                        help = "Names of players to add to the game. Defaults to Chet, Pat, and Sue")
    parser.add_argument("--seed", 
                        type = int, 
                        default = 42, 
                        help = "Seed for random number generator")
    
    args = parser.parse_args()

    main(players=args.players, seed_number=args.seed)

