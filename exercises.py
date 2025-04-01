import random
import unittest

def odds(list):
    '''self.assertEqual([1, 3, 5], odds([1, 2, 3, 4, 5]))'''
    odds = [element for element in list if element % 2 == 1]
    print(odds)
    return odds

def even_squared(list):
    even_squared = [element**2 for element in list if element % 2 == 0]
    print(even_squared)
    return even_squared

def indexed_strings(list):
    indexed = [f"{index}->{element}" for index,element in enumerate(list)]
    print(indexed)
    return indexed

def sum_odds(list):
    sum_odds = sum(odds(list))
    print(sum_odds)
    return sum_odds

def squared_by_index(list):
    '''{0: 1, 1: 4, 2: 9, 3: 16}'''
    dict = {index:e**2 for index,e in enumerate(list)}
    # scris cu for ciobaesc:
    # dict = {}
    # for index, element in enumerate(list):
    #     dict[index] = element**2

    print(dict)
    return dict

# "fizz" if n|3, "buzz" if n|5, "fizz buzz" if n|3 and n|5, n as string otherwise
def fizz_buzz(n):
    # fizz_buzz=[]
    # for i in range(1,n+1):
    #     fizz_buzz.append(fizz_buzz_gen(i))
    # return fizz_buzz
    return [fizz_buzz_gen(i) for i in range(1,n+1)]

def fizz_buzz_gen(i):
    if i % 3 == 0 and i % 5 == 0:
        return "fizz buzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str(i)

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
        self.assertEqual([
            "1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz",
            "11", "fizz", "13", "14", "fizz buzz"], fizz_buzz(15))
    # todo write a unit test then implement the following functionality
    #  double_odds(list) returns a list with the odd elements, doubled.

if __name__ == '__main__':
    unittest.main()