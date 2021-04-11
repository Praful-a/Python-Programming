# Program to sum all the items in a list
## 1st Method  ##
# def sum_all_item(li):
#     sum = 0
#     for i in range(len(li)):
#         sum += li[i]
#     return sum
# print(sum_all_item([1,2,3,4,5]))

def sum_all_item(li):
    sum = 0
    for i in li:
        sum += i
    return sum
print(sum_all_item([1,2,3,4,5]))
