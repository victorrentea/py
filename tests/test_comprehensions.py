# File: tests/test_comprehensions.py

import unittest

from exercises import odds


class TestOddsFunction(unittest.TestCase):

    def test_odds(self):
        self.assertEqual(odds([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(odds([2, 4, 6, 8]), [])
        self.assertEqual(odds([]), [])
        self.assertEqual(odds([-5, -4, -3, -2, -1, 0, 1]), [-5, -3, -1, 1])
