import random
import unittest


def odds(list):
    odds = []
    for n in list:
        if n % 2 != 0:
            odds.append(n)
    print(odds)
    return odds

def even_squared(list):
    even_squared = []
    for n in list:
        if n % 2 == 0:
            even_squared.append(n**2)
    print(even_squared)
    return even_squared

def indexed_strings(list):
    indexed = []
    for index,n in enumerate(list):
        indexed.append(f"{index}->{n}")
    print(indexed)
    return indexed

def sum_odds(list):
    sum_odds = 0
    for n in list:
        if n % 2 != 0:
            sum_odds += n
    print(sum_odds)
    return sum_odds

def squared_by_index(list):
    dict = {}
    for index,n in enumerate(list):
        dict[index] = n**2
    print(dict)
    return dict

# "fizz" if |3, "buzz" if |5, "fizz buzz" if |15
def fizz_buzz(n):
    fizz_buzz=[]
    for n in range(1, n+1):
        if n % 3 == 0 and n % 5 == 0:
            fizz_buzz.append("fizz buzz")
        elif n % 3 == 0:
            fizz_buzz.append("fizz")
        elif n % 5 == 0:
            fizz_buzz.append("buzz")
        else:
            fizz_buzz.append(f"{n}")
    return fizz_buzz



class Tests(unittest.TestCase):

    def test_odds(self):
        self.assertEqual([1, 3, 5], odds([1, 2, 3, 4, 5]))

    def test_even_squared_with_positive_numbers(self):
        self.assertEqual([4, 16], even_squared([1, 2, 3, 4]))

    def test_indexed_strings(self):
        self.assertEqual(["0->5", "1->6", "2->7"], indexed_strings([5,6,7]))

    def test_sum_odds(self):
        self.assertEqual(4, sum_odds([1, 2, 3, 4]))

    def test_squared_by_index(self):
        self.assertEqual({0: 1, 1: 4, 2: 9, 3: 16}, squared_by_index([1, 2, 3, 4]))

    def test_fizz_buzz(self):
        self.assertEqual(["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"], fizz_buzz(10))
