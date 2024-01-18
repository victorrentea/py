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


class X:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __str__(self):
        return f"{self.a} {self.b}"
map = {}
map[X()] = 1

map[X()] = 2

print(map)