# Calculate lenght of the string
# string = "Python"
# count = 0
# for i in string:
#     count += 1
# print(count)

# count the frequency of each character in string
## Naive method
# def count_freq(str):
#     dict = {}
#     for n in str:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(count_freq("geeksforgeeks"))

## using collections.Counter()
# from collections import Counter
# test_str = "geeksforgeeks"
# res = Counter(test_str)
# print("Count of all characters in GeeksforGeeks is :\n " + str(res))

# using dictionary get method
# test_str = "GeeksforGeeks"
# res = {}
# for keys in test_str:
#     res[keys] = res.get(keys, 0) + 1
# print("Count of all characters in GeeksforGeeks is : \n" + str(res))

## using set + count method
# test_str = "GeeksforGeeks"
# res = {i : test_str.count(i) for i in set(test_str)}
# print("The count of all characters in GeeksforGeeks is :\n" + str(res))

# def string_both_ends(str):
#     if len(str) < 2:
#         return "Empty String"
#     return str[0:2] + str[-2:]
# 
# print(string_both_ends("w3resource"))
# print(string_both_ends("w3"))
# print(string_both_ends("w"))
