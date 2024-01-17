import random
from io import StringIO
import sys

from trivia import Game
from trivia_original import GameOriginal

def capture_output(f):
    captured_output = StringIO()  # Make StringIO.
    sys.stdout = captured_output  # Redirect stdout.
    f()  # Call function.
    sys.stdout = sys.__stdout__  # Reset redirect.
    return captured_output


def play_game(game, seed):
    random.seed(seed)
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(random.randint(1,6))

        if random.randint(1, 9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break

from unittest import TestCase

# for i from 1 to 100
for seed in range(1, 1000):
    expected = capture_output(lambda: play_game(GameOriginal(), seed))
    actual = capture_output(lambda: play_game(Game(), seed))
    TestCase.maxDiff = None
    TestCase().assertMultiLineEqual(expected.getvalue(), actual.getvalue(), f"Failed for seed: {seed}")