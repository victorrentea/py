from itertools import groupby


class Yatzy:

    @staticmethod
    def chance(dice: list[int]):
        return sum(dice)

    @staticmethod
    def sum_if(dice, x):
        return sum(die for die in dice if die == x)

    @staticmethod
    def ones(dice: list[int]):
        return Yatzy.sum_if(dice, 1)

    @staticmethod
    def twos(dice: list[int]):
        return Yatzy.sum_if(dice, 2)

    @staticmethod
    def threes(dice: list[int]):
        return Yatzy.sum_if(dice, 3)

    @staticmethod
    def fours(dice: list[int]):
        return Yatzy.sum_if(dice, 4)

    @staticmethod
    def fives(dice: list[int]):
        return Yatzy.sum_if(dice, 5)

    @staticmethod
    def sixes(dice: list[int]):
        return Yatzy.sum_if(dice, 6)

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    @staticmethod
    def score_pair(dice: list[int]):
        freq = {die: len(list(n)) for die, n in groupby(sorted(dice))}
        d2 = [die for die, count in freq.items() if count >= 2]
        return 2 * max(d2) if d2 else 0

    @staticmethod
    def two_pair(dice: list[int]):
        freq = {die: len(list(n)) for die, n in groupby(sorted(dice))}
        d2 = [die for die, count in freq.items() if count >= 2]
        return 2 * sum(d2) if d2 and len(d2) == 2 else 0

    @staticmethod
    def four_of_a_kind(dice: list[int]):
        freq = {die: len(list(n)) for die, n in groupby(sorted(dice))}
        d2 = [die for die, count in freq.items() if count >= 4]
        return 4 * d2[0] if d2 else 0

    @staticmethod
    def three_of_a_kind(dice: list[int]):
        freq = {die: len(list(n)) for die, n in groupby(sorted(dice))}
        d2 = [die for die, count in freq.items() if count >= 3]
        return 3 * d2[0] if d2 else 0

    @staticmethod
    def smallStraight(dice: list[int]):
        if len(set(dice)) != 5:
            return 0
        return 15 if max(dice) == 5 else 0

    @staticmethod
    def largeStraight(dice: list[int]):
        if len(set(dice)) != 5:
            return 0
        return 20 if min(dice) == 2 else 0

    @staticmethod
    def fullHouse(dice: list[int]):
        freq = {die: len(list(n)) for die, n in groupby(sorted(dice))}
        if set(freq.values()) != {2, 3}:
            return 0
        dice23 = [die for die, _ in sorted(freq.items(), key=lambda x: x[1])]
        return 2 * dice23[0] + 3 * dice23[1]
