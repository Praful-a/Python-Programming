# # 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# # Sample data : {'1':['a','b'], '2':['c','d']}
# # Expected Output:
# # ac
# # ad
# # bc
# # bd
# import itertools
# d = {'1': ['a', 'b'], '2': ['c', 'd']}
# for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
#     print(''.join(combo))
# # or
# d = {'1': ['a', 'b'], '2': ['c', 'd']}
# l1 = d['1']
# l2 = d['2']
# for i in l1:
#     for j in l2:
#         print(i, j, sep='')

# # 22. Write a Python program to find the highest 3 values in a dictionary.
# from heapq import nlargest
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest)
# # or
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# value = [v for v in my_dict.values()]
# n = len(value)
# for i in range(n):
#     for j in range(1, n-i):
#         if value[j-1] < value[j]:
#             value[j-1], value[j] = value[j], value[j-1]
# d = value[0:3]
# print(d)
# g = []
# for h in my_dict:
#     for m in d:
#         if my_dict[h] == m:
#             g.append(h)
# print(set(g))

# # 23. Write a Python program to combine values in python list of dictionaries.
# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {
#     'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(result)
