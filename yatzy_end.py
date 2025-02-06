'''
Ones, Twos, Threes, Fours, Fives, Sixes:
The player scores the sum of the dice that reads one, two, three, four, five or six, respectively. For example:
1,1,2,4,4 placed on “fours” scores 8 (4+4)
2,3,2,5,1 placed on “twos” scores 4 (2+2)
3,3,3,4,5 placed on “ones” scores 0
1,1,3,4,5 placed on “ones” scores 2 (1+1)
'''


class Yatzy:
    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def chance(self):
        '''
        The player scores the sum of all dice, no matter what they read. For example:
        1,1,3,3,6 placed on “chance” scores 14 (1+1+3+3+6)
        4,5,5,6,1 placed on “chance” scores 21 (4+5+5+6+1)
        '''
        return sum(self.dice)

    def yatzy(self):  # TODO later
        '''
        If all dice have the same number, the player scores 50 points. For example:
        1,1,1,1,1 placed on “yatzy” scores 50
        1,1,1,2,1 placed on “yatzy” scores 0
        '''
        return 50 if len(set(self.dice)) ==1 else 0

    def ones(self):
        return sum([die for die in self.dice if die == 1])

    def twos(self):
        return sum([die for die in self.dice if die == 2])

    def threes(self):
        return sum([die for die in self.dice if die == 3])

    def fours(self):
        return sum([die for die in self.dice if die == 4])

    def fives(self):
        return sum([die for die in self.dice if die == 5])

    def sixes(self):
        return sum([die for die in self.dice if die == 6])

    def one_pair(self):
        '''
        The player scores the sum of the two highest matching dice.
        For example, when placed on “pair”:
        1,2,3,4,5 scores 0 (no pair)
        3,3,3,4,4 scores 8 (4+4)
        1,1,6,2,6 scores 12 (6+6)
        3,3,3,4,1 scores 6 (3+3)
        3,3,3,3,1 scores 6 (3+3)
        '''
        # go down from 6 to 1 go through the array and see and count how many occurences you find
        # for i in range(6, 0, -1):
        #     if self.dice.count(i) >= 2:
        #         return i * 2
        # return 0

        # return sum(repeating) * 2 if len(repeating) == 2 else 0
        return max([0] + [k for k, v in self.frequencies().items() if v >= 2]) * 2

    def two_pair(self):
        '''
        If there are two pairs of dice with the same number, the player scores the sum of these dice. For example, when placed on “two pairs”:
        1,1,2,3,3 scores 8 (1+1+3+3) => {1=>2, 2=>1, 3=>2}
        1,1,2,3,4 scores 0
        1,1,2,2,2 scores 6 (1+1+2+2) => {1=>2, 2=>3}
        3,3,3,3,1 scores 0
        '''
        repeating = [k for k, v in self.frequencies().items() if v >= 2]
        return sum(repeating) * 2 if len(repeating) == 2 else 0

    def frequencies(self):
        return {value: self.dice.count(value) for value in set(self.dice)}

    def three_of_a_kind(self):
        '''
        if there are three dice with the same number, the player scores the sum of these dice. For example, when placed on “three of a kind”:
        3,3,3,4,5 scores 9 (3+3+3)
        3,3,4,5,6 scores 0
        3,3,3,3,1 scores 9 (3+3+3)
        '''
        repeating = [k for k, v in self.frequencies().items() if v >= 3]
        return sum(repeating) * 3 if repeating else 0

    def four_of_a_kind(self):
        '''
        If there are four dice with the same number, the player scores the sum of these dice. For example, when placed on “four of a kind”:
        2,2,2,2,5 scores 8 (2+2+2+2)
        2,2,2,5,5 scores 0
        2,2,2,2,2 scores 8 (2+2+2+2)
        '''
        # return sum(repeating) * 4 if repeating else 0
        return next(iter([k for k, v in self.frequencies().items() if v >= 4]), 0) * 4

    def smallStraight(self):
        '''
        When placed on “small straight”, if the dice read
        1,2,3,4,5,
        the player scores 15 (the sum of all the dice).
        '''
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def largeStraight(self):
        '''
        When placed on “large straight”, if the dice read
        2,3,4,5,6,
        the player scores 20 (the sum of all the dice).
        '''
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def fullHouse(self):
        '''
        If the dice are two of a kind and three of a kind, the player scores the sum of all the dice.
        For example, when placed on “full house”:
        1,1,2,2,2 scores 8 (1+1+2+2+2)
        2,2,3,3,4 scores 0
        2,2,2,3,4 scores 0
        4,4,4,4,4 scores 0
        '''
        return sum(self.dice) if sorted(self.frequencies().values()) == [2, 3] else 0


import unittest


# These unit tests can be run using the py.test framework
# available from http://pytest.org/

class YatziTest(unittest.TestCase):

    def test_chance(self):
        expected = 15
        actual = Yatzy(2, 3, 4, 5, 1).chance()
        assert expected == actual
        assert 16 == Yatzy(3, 3, 4, 5, 1).chance()

    def test_yatzy_scores_50(self):
        expected = 50
        actual = Yatzy(4, 4, 4, 4, 4).yatzy()
        assert expected == actual
        assert 50 == Yatzy(6, 6, 6, 6, 6).yatzy()
        assert 0 == Yatzy(6, 6, 6, 6, 3).yatzy()

    def test_ones(self):
        assert 1 == Yatzy(1, 2, 3, 4, 5).ones()
        assert 2 == Yatzy(1, 2, 1, 4, 5).ones()
        assert 0 == Yatzy(6, 2, 2, 4, 5).ones()
        assert 4 == Yatzy(1, 2, 1, 1, 1).ones()

    def test_twos(self):
        assert 4 == Yatzy(1, 2, 3, 2, 6).twos()
        assert 10 == Yatzy(2, 2, 2, 2, 2).twos()

    def test_threes(self):
        assert 6 == Yatzy(1, 2, 3, 2, 3).threes()
        assert 12 == Yatzy(2, 3, 3, 3, 3).threes()

    def test_fours(self):
        assert 12 == Yatzy(4, 4, 4, 5, 5).fours()
        assert 8 == Yatzy(4, 4, 5, 5, 5).fours()
        assert 4 == Yatzy(4, 5, 5, 5, 5).fours()

    def test_fives(self):
        assert 10 == Yatzy(4, 4, 4, 5, 5).fives()
        assert 15 == Yatzy(4, 4, 5, 5, 5).fives()
        assert 20 == Yatzy(4, 5, 5, 5, 5).fives()

    def test_sixes_test(self):
        assert 0 == Yatzy(4, 4, 4, 5, 5).sixes()
        assert 6 == Yatzy(4, 4, 6, 5, 5).sixes()
        assert 18 == Yatzy(6, 5, 6, 6, 5).sixes()

    def test_one_pair_returns_0_for_no_pair(self):
        assert 0 == Yatzy(3, 4, 1, 5, 6).one_pair()

    def test_one_pair(self):
        assert 6 == Yatzy(3, 4, 3, 5, 6).one_pair()
        assert 10 == Yatzy(5, 3, 3, 3, 5).one_pair()
        assert 12 == Yatzy(5, 3, 6, 6, 5).one_pair()

    def test_two_Pair(self):
        assert 16 == Yatzy(3, 3, 5, 4, 5).two_pair()
        assert 18 == Yatzy(3, 3, 6, 6, 6).two_pair()
        assert 0 == Yatzy(3, 3, 6, 5, 4).two_pair()

    def test_three_of_a_kind(self):
        assert 9 == Yatzy(3, 3, 3, 4, 5).three_of_a_kind()
        assert 15 == Yatzy(5, 3, 5, 4, 5).three_of_a_kind()
        assert 9 == Yatzy(3, 3, 3, 3, 5).three_of_a_kind()

    def test_four_of_a_knd(self):
        assert 12 == Yatzy(3, 3, 3, 3, 5).four_of_a_kind()
        assert 20 == Yatzy(5, 5, 5, 4, 5).four_of_a_kind()
        assert 12 == Yatzy(3, 3, 3, 3, 3).four_of_a_kind()
        assert 0 == Yatzy(3, 3, 3, 2, 1).four_of_a_kind()

    def test_smallStraight(self):
        # assert [1, 2, 3, 4, 5] == [1, 2, 3, 4, 5]
        assert 15 == Yatzy(1, 2, 3, 4, 5).smallStraight()
        assert 15 == Yatzy(2, 3, 4, 5, 1).smallStraight()
        assert 0 == Yatzy(1, 2, 2, 4, 5).smallStraight()

    def test_largeStraight(self):
        assert 20 == Yatzy(6, 2, 3, 4, 5).largeStraight()
        assert 20 == Yatzy(2, 3, 4, 5, 6).largeStraight()
        assert 0 == Yatzy(1, 2, 2, 4, 5).largeStraight()

    def test_fullHouse(self):
        assert 18 == Yatzy(6, 2, 2, 2, 6).fullHouse()
        assert 0 == Yatzy(2, 3, 4, 5, 6).fullHouse()
