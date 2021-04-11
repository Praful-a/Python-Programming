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
def mul_all_items(l):
    product = 1
    for i in l:
        product *= i
    return product
print(mul_all_items([1,2,3]))
