from dataclasses import dataclass


@dataclass(frozen=True)
class A:

    name: str

    list: list[str]

    def __str__(self):
        return f"{self.name} {self.list}"

    def stuff(self):
        self.list.append("AAA")



if __name__ == '__main__':
    a = A("name",["a","b"])
    # a.name = "x"
    a.list.append("AAA")

    print(a)


x=True
coll=[]
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