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
