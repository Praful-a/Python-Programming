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
"""Fisher-Yates shuffle Algorithm"""
# import random
# test_lst = [1,4,5,6,3]
# print("The original list is : " + str(test_lst))
# for i in range(len(test_lst)-1, 0, -1):
#     j = random.randint(0, i+1)
#     # swap arr[i] with the element at random index
#     test_lst[i], test_lst[j] = test_lst[j], test_lst[i]
# print("The shuffled list is : " + str(test_lst))
"""using random shuffle method"""
# from random import shuffle
# lst = [1,2,3,4,5]
# shuffle(lst)
# print(lst)
"""Using random.sample()"""
# import random
# test_lst = [1,4,5,6,3]
# print("The original list is : " + str(test_lst))
# res = random.sample(test_lst, len(test_lst))
# print('The shuffled list is : ' + str(res))

"""print a list of first and last 5 elements where the values
are square of numbers between 1 and 30."""
"""First method"""
# def generate():
#     lst = []
#     for i in range(1, 31):
#         lst.append(i**2)
#     print(lst[:5], end='')
#     print(lst[-5:])
# generate()
"""Second method"""
# def generate():
#     lst = []
#     for i in range(1, 31):
#         if i <= 5 or i > 25:
#             lst.append(i**2)
#     print(lst)
# generate()

"""Program to generate all permutations of a list"""
"""Using permutations method"""
# import itertools
# print(list(itertools.permutations([1,2,3])))
"""without using predefined methods."""
# lst = [1,2,3]
# for i in range()

"""Get the difference between the two lists."""
"""using simple method"""
# def difference(l1, l2):
#     li = []
#     for i in l1:
#         if i not in l2:
#             li.append(i)
#     for j in l2:
#         if j not in l1:
#             li.append(j)
#     return li
# lst1 = [1,2,3,4,5]
# lst2 = [4,5,6,7,1]
# print(difference(lst1, lst2))
"""using set"""
# def difference(l1, l2):
#     diff_l1_l2 = list(set(l1) - set(l2))
#     diff_l2_l1 = list(set(l2) - set(l1))
#     total_diff = diff_l1_l2 + diff_l2_l1
#     return total_diff
#
# lst1 = [1,2,3,4,5]
# lst2 = [4,5,6,7,1]
# print(difference(lst1, lst2))

"""Access the index of a list"""
"""First Method"""
# def access_index(li):
#     for i in range(len(li)):
#         print("{} : {}".format(i, li[i]))
#
# lst = [32, 47, -50, 53, -9]
# access_index(lst)
"""Second Method"""
# def access_index(li):
#     for index, value in enumerate(li):
#         print("{} : {}".format(index, value))
# lst = [32, 45, 100, 90, -1, 2]
# access_index(lst)

"""Convert a list of character into string."""
"""First Method"""
# lst = ['P', 'Y', 'T', 'H', 'O', 'N']
# lst1 = ''.join(lst)
# print(lst1)
"""Second Method"""
# def join(lst):
#     str = ""
#     for i in range(len(lst)):
#             str += lst[i]
#     return str
#
# lst = ['P', 'Y', 'T', 'H', 'O', 'N']
# print(join(lst))
