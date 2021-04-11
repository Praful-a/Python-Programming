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
