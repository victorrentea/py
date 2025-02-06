

class Yatzy:
    def __init__(self, d1=0, d2=0, d3=0, d4=0, d5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    def chance(self):
        '''
        The player scores the sum of all dice, no matter what they read. For example:
        1,1,3,3,6 placed on “chance” scores 14 (1+1+3+3+6)
        4,5,5,6,1 placed on “chance” scores 21 (4+5+5+6+1)
        '''
        total = 0
        total += self.dice[0]
        total += self.dice[1]
        total += self.dice[2]
        total += self.dice[3]
        total += self.dice[4]
        return total

    def yatzy(self):
        '''
        If all dice have the same number, the player scores 50 points. For example:
        1,1,1,1,1 placed on “yatzy” scores 50
        1,1,1,2,1 placed on “yatzy” scores 0
        '''
        counts = [0] * (len(self.dice) + 1)
        for die in self.dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0


    '''
    Ones, Twos, Threes, Fours, Fives, Sixes:
    The player scores the sum of the dice that reads one, two, three, four, five or six, respectively. For example:
    1,1,2,4,4 placed on “fours” scores 8 (4+4)
    2,3,2,5,1 placed on “twos” scores 4 (2+2)
    3,3,3,4,5 placed on “ones” scores 0
    '''
    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 1):
            sum += 1
        if (d2 == 1):
            sum += 1
        if (d3 == 1):
            sum += 1
        if (d4 == 1):
            sum += 1
        if (d5 == 1):
            sum += 1
        return sum

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 2):
            sum += 2
        if (d2 == 2):
            sum += 2
        if (d3 == 2):
            sum += 2
        if (d4 == 2):
            sum += 2
        if (d5 == 2):
            sum += 2
        return sum

    def threes(self):
        s = 0
        if (d[0] == 3):
            s += 3
        if (d[1] == 3):
            s += 3
        if (d[2] == 3):
            s += 3
        if (d[3] == 3):
            s += 3
        if (d[4] == 3):
            s += 3
        return s

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s
    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    def score_pair(self):
        '''
        The player scores the sum of the two highest matching dice. For example, when placed on “pair”:
        1,2,3,4,5 scores 0
        3,3,3,4,4 scores 8 (4+4)
        1,1,6,2,6 scores 12 (6+6)
        3,3,3,4,1 scores 6 (3+3)
        3,3,3,3,1 scores 6 (3+3)
        '''
        return 0

    def two_pair(self):
        '''
        If there are two pairs of dice with the same number, the player scores the sum of these dice. For example, when placed on “two pairs”:
        1,1,2,3,3 scores 8 (1+1+3+3)
        1,1,2,3,4 scores 0
        1,1,2,2,2 scores 6 (1+1+2+2)
        3,3,3,3,1 scores 0
        '''
        return 0

    def three_of_a_kind(self):
        '''
        if there are three dice with the same number, the player scores the sum of these dice. For example, when placed on “three of a kind”:
        3,3,3,4,5 scores 9 (3+3+3)
        3,3,4,5,6 scores 0
        3,3,3,3,1 scores 9 (3+3+3)
        '''
        return 0

    def four_of_a_kind(self):
        '''
        If there are four dice with the same number, the player scores the sum of these dice. For example, when placed on “four of a kind”:
        2,2,2,2,5 scores 8 (2+2+2+2)
        2,2,2,5,5 scores 0
        2,2,2,2,2 scores 8 (2+2+2+2)
        '''
        return 0 # TODO

    def smallStraight(self):
        '''
        When placed on “small straight”, if the dice read
        1,2,3,4,5,
        the player scores 15 (the sum of all the dice).
        '''
        return 0 # TODO

    def largeStraight(self):
        '''
        When placed on “large straight”, if the dice read
        2,3,4,5,6,
        the player scores 20 (the sum of all the dice).
        '''
        return 0 # TODO

    def fullHouse(self):
        '''
        If the dice are two of a kind and three of a kind, the player scores the sum of all the dice. For example, when placed on “full house”:
        1,1,2,2,2 scores 8 (1+1+2+2+2)
        2,2,3,3,4 scores 0
        4,4,4,4,4 scores 0
        '''
        return 0 # TODO


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


    def test_1s(self):
        assert Yatzy.ones(1, 2, 3, 4, 5) == 1
        assert 2 == Yatzy.ones(1, 2, 1, 4, 5)
        assert 0 == Yatzy.ones(6, 2, 2, 4, 5)
        assert 4 == Yatzy.ones(1, 2, 1, 1, 1)


    def test_2s(self):
        assert 4 == Yatzy.twos(1, 2, 3, 2, 6)
        assert 10 == Yatzy.twos(2, 2, 2, 2, 2)


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


    def test_one_pair(self):
        assert 6 == Yatzy(3, 4, 3, 5, 6).score_pair()
        assert 10 == Yatzy(5, 3, 3, 3, 5).score_pair()
        assert 12 == Yatzy(5, 3, 6, 6, 5).score_pair()


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

