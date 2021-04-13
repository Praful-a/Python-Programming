"""Print specified list after removing the 0th, 4th and 5th elements."""
"""using list comprehension"""
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)
"""using function"""
# def remove(l):
#     l2 = []
#     for i in range(len(l)):
#         if ((i!=0) and (i!=4) and (i!=5)):
#             l2.append(l[i])
#     return l2
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(remove(color))

"""Generate a 3*4*6 3D array whose each element is *."""
# array = [[["*" for col in range(6)] for col in range(4)] for col in range(3)]
# print(array)
# print("[", end="")
# for row in range(3):
#     print("[", end="")
#     for j in range(4):
#         print("[", end="")
#         for k in range(6):
#             print("*", end=",")
#         print("]", end="")
#     print("]", end=",")
#     print(end="")
# print("]")

"""Remove even numbers from list."""
"""list comprehension"""
# def remove_even(li):
#     return [x for x in li if (x%2 != 0)]
#
# lst = [1, 2, 9, 8, 5, 77, 90, 89]
# print(remove_even(lst))
"""Using function"""
# def remove_even(li):
#     lst2 = []
#     for i in li:
#         if (i%2 != 0):
#             lst2.append(i)
#     return lst2
#
# lst = [1, 2, 9, 8, 5, 77, 90, 89]
# print(remove_even(lst))

"""Shuffle and print a specified list."""
from random import shuffle
lst = [1,2,3,4,5]
shuffle(lst)
print(lst)
