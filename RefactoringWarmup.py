from math import sqrt

def loop(numbers):
    # ssq = 0
    # for number in numbers:
    #     if number % 2 == 0:
    #         ssq += number * number

    # for number in numbers:
    #     ssq += number ** 2 if number%2==0 else 0

    # comprehensions: suma patratelor numerelor din lista daca sunt pare
    ssq = sum([n * n for n in numbers if n % 2 == 0])

    print(ssq)


if __name__ == "__main__":
    loop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])