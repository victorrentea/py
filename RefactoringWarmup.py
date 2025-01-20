from math import sqrt

DAYS_PER_WEEK = 7


# TODO: Practice Refactoring
#  * How to?
#    - Select text > Hover
#    - Right-click > Refactor
#    - Ctrl-Alt-Shift-T/^T to
#    - Keys: [Ctrl-Alt / Opt-Cmd] + [V]ariable/[M]ethod/[P]arameter/i[N]line
#  * What? // after every action undo/revert to start clean
#    - Inline[N] Variable 'b'
#    - Extract [V]ariable '1', '3 * two.g()'
#    - Extract [M]ethod 'System.out..'
#    - Inline[N] Method 'g'
#    - Extract [P]arameter '1', 'r.x()'
#    - Inline[N] Parameter 'c'
#    - Change Signature 'g': add 1 param with default as 1st arg
#    - Extract Interface 'Two'->ITwo; - Inline to Anonymous Class to destroy interface
#    - Rename 'g' -> 'h' by Shift-F6 or just edit>Alt-Enter>Rename
#    - Move Method 'g' into R
#    - Preview method/class: Ctrl-Shift-I
#    - Quickfix for->stream
#    - Change inspection severity & highlighting
#       * Download "aggressive_refactoring.xml" from https://victorrentea.ro
#       and import it in Settings>Editor>Inspections

class R:
    def __init__(self, x):
        self._x = x


class One:
    def __init__(self, two):
        self.two = two

    def f(self):
        self.two.g(DAYS_PER_WEEK, R(3))
        return 2 * self.two.g(1, R(3))


class Two:
    def g(self, i, r):
        b = 2
        self.ff(b)
        return i + b + r.x

    def ff(self, b):
        print(f"b={b}")

    def unknown(self):
        self.ff(987)


def loop():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ssq = 0
    for number in numbers:
        if number % 2 == 0:
            ssq += number * number
    print(sqrt(ssq))


if __name__ == "__main__":
    print(One(Two()).f())
    loop()
