import re
from dataclasses import dataclass
from enum import Enum

def f(a,b):
    return a or b or None

if __name__ == '__main__':
    print(f(1,2))
    print(f("1","2"))
    print(f( None,2))
    print(f( None,2))
    print(f( None,None))
