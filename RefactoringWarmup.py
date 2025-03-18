from math import sqrt

ANSWER_OF_LIFE = 42
UNGARIA = ""

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
        self.x = x


class Two:
    def sanitize_fulfillment_data(self, r:R, p:int=ANSWER_OF_LIFE):
        b = 2
        
        print(f"b={b}")

        return p + b + r.x


    def unknown(self):
        print(f"b={987} " + UNGARIA) # "" = ungaria

class One:
    def __init__(self, two:Two):
        self.two = two

    def f(self):
        return 2 * self.two.sanitize_fulfillment_data(R(3))


def loop():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ssq = sum([x*x for x in numbers if x %2 == 0])
    print(sqrt(ssq))


if __name__ == "__main__":
    print(One(Two()).f())
    (Two()).sanitize_fulfillment_data(R(),7) # nu 42 si 7 nr sfant
    loop()