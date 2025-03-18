# import re
# from dataclasses import dataclass
# from enum import Enum


# @dataclass(frozen=True)
# class A:
#     name: str

#     list: list[str]

#     def __str__(self):
#         return f"{self.name} {self.list}"

#     def stuff(self):
#         self.list.append("AAA")


# if __name__ == '__main__':
#     a = A("name", ["a", "b"])

#     # a.name = "x"
#     a.list.append("AAA")

#     print(a)

# x = True
# coll = []
# if (x and coll):
#     print("x and coll")


# # @dataclass(unsafe_hash=True)
# class X:
#     # a: int
#     def __init__(self, a):
#         self.a = a


# set = set()
# set.add(X(1))
# set.add(X(1))
# print(set)


# # typealias IP = str
# # from typing import TypeAlias
# # CouponId: TypeAlias = str
# # CustomerId: TypeAlias = str


# class CouponId(str):
#     pass


# class CustomerId(str):
#     pass


# def foo(coupon: CouponId, c: CustomerId):
#     pass


# foo(CouponId("1"), "2")


# map: dict[int,list[int]] = {}



# print(re.search(r"hostname: '(.+)'", "blabla"))

# class A(Enum):
#     A =1
#     B,
#     C,





print("-----------------")
def append_to_list(lst, item):
    lst.append(item)
    # lst=null

list = [1,2,3]
print(list)
append_to_list(list, 4)
print(list)


# ll = [0]*11
# ll[10] = 'a'


# x = None + 3



# print(list(range(1, 10, 3)))
end = 3
for i in range(1, end, 7):
    page_start = i
    page_end = i + 7 if i + 7 < end else end
    print(page_start ,  page_end)


resultset = [1,2,3,4,5] # 200 MB imagine

alta_lista_pe_heap=[x for x in resultset if x % 2==0] # 100MB - RAU!
def it(): return (x for x in resultset if x % 2 == 0) # 0b - bine! generatori

for x in it(): print(x)
print("--- ", next(it))
for x in it(): print(x)