# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)
#
#
# my_nums = square_numbers([1, 2, 3, 4, 5])

my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(list(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# Now if i do it again then it will give us an error
# print(next(my_nums))

# for num in my_nums:
#     print(num)
