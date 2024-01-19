import re
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class A:
    name: str

    list: list[str]

    def __str__(self):
        return f"{self.name} {self.list}"

    def stuff(self):
        self.list.append("AAA")


if __name__ == '__main__':
    a = A("name", ["a", "b"])

    # a.name = "x"
    a.list.append("AAA")

    print(a)

x = True
coll = []
if (x and coll):
    print("x and coll")


# @dataclass(unsafe_hash=True)
class X:
    # a: int
    def __init__(self, a):
        self.a = a


set = set()
set.add(X(1))
set.add(X(1))
print(set)


# typealias IP = str
# from typing import TypeAlias
# CouponId: TypeAlias = str
# CustomerId: TypeAlias = str


class CouponId(str):
    pass


class CustomerId(str):
    pass


def foo(coupon: CouponId, c: CustomerId):
    pass


foo(CouponId("1"), "2")


map: dict[int,list[int]] = {}



print(re.search(r"hostname: '(.+)'", "blabla"))

class A(Enum):
    A =1
    B,
    C,