# Tuples are immutable data types in python means you can not change it once you defined.
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
#
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
#
# print(list_1)
# print(list_2)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')

tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Now here we got an error because you can not change tuples.
tuple_1[0] = 'Art'
print(tuple_1)
print(tuple_2)

# creating empty tuples

empty_tuple = ()
empty_tuple = tuple()
