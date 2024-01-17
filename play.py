from dataclasses import dataclass


# @dataclass(frozen=True)
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

