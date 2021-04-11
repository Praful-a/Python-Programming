# Program to sum all the items in a list
## 1st Method  ##
# def sum_all_item(li):
#     sum = 0
#     for i in range(len(li)):
#         sum += li[i]
#     return sum
# print(sum_all_item([1,2,3,4,5]))
### Second Method ####
# def sum_all_item(li):
#     sum = 0
#     for i in li:
#         sum += i
#     return sum
# print(sum_all_item([1,2,3,4,5]))

# multiplies all the items in a list
"""First Method"""
# def mul_all_items(l):
#     product = 1
#     for i in range(len(l)):
#         product *= l[i]
#     return product
# print(mul_all_items([1,2,3,4,5]))
"""Second Method"""
# def mul_all_items(l):
#     product = 1
#     for i in l:
#         product *= i
#     return product
# print(mul_all_items([1,2,3]))

# Get the largest number from a list
"""First Method"""
# def get_largest(l):
#     max = l[0]
#     for i in range(len(l)):
#         if l[i] > max:
#             max = l[i]
#     return max
# print(get_largest([-1, 0, 2, 3, 4]))
"""Second Method"""
# def get_largest(l):
#     max = l[0]
#     for i in l:
#         if i > max:
#             max = i
#     return max
# print(get_largest([-1, 0, 2, 3, 4]))
"""Third Method"""
# def get_largest(l):
#     max1 = max(l)
#     return max1
# print(get_largest([-1, 0, 2, 3, 4]))

# Get the smallest number from list.
"""First Method"""
# def get_smallest(l):
#     min = l[0]
#     for i in range(len(l)):
#         if l[i] < min:
#             min = l[i]
#     return min
# print(get_smallest([-1, 0, 2, 3, 4]))
"""Second Method"""
# def get_smallest(l):
#     min = l[0]
#     for i in l:
#         if i < min:
#             min = i
#     return min
# print(get_smallest([-1, 0, 2, 3, 4]))
"""Third Method"""
# def get_smallest(l):
#     max1 = min(l)
#     return max1
# print(get_smallest([-1, 0, 2, 3, 4]))

"""Count the number of strings where the string length 2
or more and the first and last character are same from a given
list of strings."""
"""First Method"""
# def count_string(li):
#     count = 0
#     for i in li:
#         if len(i) >= 2:
#             if i[0] == i[-1]:
#                 count += 1
#     return count
# print(count_string(['aba', 'xyz', 'aba', '1221']))

"""Sort in increasing order by the last element in each tuple
from a given list of non-empty tuples."""
"""using sorted Method"""
# def last(n):
#     return n[-1]
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
# print(sort_list_last( [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
"""Using Bubble sort"""
# def sort_Tuple(tup):
#     lst = len(tup)
#     for i in range(0, lst):
#         for j in range(0, lst-i-1):
#             if (tup[j][-1] > tup[j+1][-1]):
#                 temp = tup[j]
#                 tup[j] = tup[j+1]
#                 tup[j+1] = temp
#     return tup
# tup =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sort_Tuple(tup))
"""Using sort method"""
# def sort_Tuple(tup):
#     tup.sort(key=lambda x: x[-1])
#     return tup
# tup =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sort_Tuple(tup))

"""Remove Duplicates from  a list."""
"""First Method"""
# def remove_duplicate(li):
#     dup_items = set()
#     uniq_items = []
#     for x in li:
#         if x not in dup_items:
#             uniq_items.append(x)
#             dup_items.add(x)
#     return dup_items
# lst = [10, 20, 30, 40, 50, 60, 10]
# print(list(remove_duplicate(lst)))
"""Second Method"""
# def remove_duplicate(li):
#     lst = []
#     for i in li:
#         if i not in lst:
#             lst.append(i)
#     return lst
# lst = [10, 20, 30, 40, 50, 60, 10]
# print(list(remove_duplicate(lst)))

"""Check list is empty or not."""
def check_list_empty(li):
    if li:
        print("list is not empty!")
    else:
        print("list is empty!")

check_list_empty([])
check_list_empty([1])
