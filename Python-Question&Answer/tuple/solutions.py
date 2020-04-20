# 1. Write a Python program to create a tuple.
from copy import deepcopy
x = ()
print(x)

tuple = tuple()
print(tuple)

# 2. Write a Python program to create a tuple with different data types.
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# 3. Write a Python program to create a tuple with numbers and print one item.
tuple = 5, 4, 12, 1, 2, 3
print(tuple)
tuplex = 5,
print(tuplex)

# 4. Write a Python program to unpack a tuple in several variables.
# create a tuple
x = (4, 5, 6)
# Unpacking the tuple
n1, n2, n3 = x
print(x)
print(n1+n2+n3)
# Unpacking tuples into variable must all variables are equal to the tuple's elements
n1, n2, n3, n4 = x

# 5. Write a Python program to add an item in a tuple.
# create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
# adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
# converting the tuple to list
listx = list(tuplex)
# use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

# 6. Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
print(''.join(tup))

# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.
tup = (4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3, 30)
print(tup[5])
print(tup[-4])

# 8. Write a Python program to create the colon of a tuple.
# create a tuple
tuplex = ("HELLO", 5, [], True)
print(tuplex)
# make a copy of a tuple using deepcopy() function
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)

# 9. Write a Python program to find the repeated items of a tuple.
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(tuplex)
# return the number of times it appears in the tuple.
count = tuplex.count(4)
print(count)

# 10. Write a Python program to check whether an element exists within a tuple.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print("r" in tuplex)
print(5 in tuplex)

# 11. Write a Python program to convert a list to a tuple.
l = [1, 2, 3, 4, 5]
print(tuple(l))

# 12. Write a Python program to remove an item from a tuple.
# create a tuple
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
# tuples are immutable, so you can not remove elements
# using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
# converting the tuple to list
listx = list(tuplex)
# use different ways to remove an item of the list
listx.remove("c")
# converting the tuple to list
tuplex = tuple(listx)
print(tuplex)

# 13. Write a Python program to slice a tuple.
tup = (1, 2, 3, 4, 5)
print(tup[1:2])
print(tup[1:-3])

# 14. Write a Python program to find the index of an item of a tuple.
# create a tuple
tuplex = tuple("index tuple")
print(tuplex)
# get index of the first item whose value is passed as parameter
index = tuplex.index("p")
print(index)
# define the index from which you want to search
index = tuplex.index("p", 5)
print(index)
# define the segment of the tuple to be searched
index = tuplex.index("e", 3, 6)
print(index)
# if item not exists in the tuple return ValueError Exception
index = tuplex.index("y")

# 15. Write a Python program to find the length of a tuple.
tup = (1, 12, 11, 13)
print(len(tup))

# 16. Write a Python program to convert a tuple to a dictionary.
tuplex = ((2, "w"), (3, "r"))
print(dict((y, x) for x, y in tuplex))

# 17. Write a Python program to unzip a list of tuples into individual lists.
l = [(1, 2), (3, 4), (8, 9)]
printlist((zip(*l)))

# 18. Write a Python program to reverse a tuple.
# create a tuple
x = ("w3resource")
# Reversed the tuple
y = reversed(x)
print(tuple(y))
# create another tuple
x = (5, 10, 15, 20)
# Reversed the tuple
y = reversed(x)
print(tuple(y))

# 19. Write a Python program to convert a list of tuples into a dictionary.
tup = ((1, "r"), (2, "t"))
print(dict(tup))

# 20. Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)
tup = (100, 200, 300)
print("This is tuple =", tup)
print("This is tuple = {}".format(tup))
print(f"This is tuple = {tup}")

# 21. Write a Python program to replace last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
tup = ([t[:-1] + (100,) for t in l])
print(tup)

# 22. Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
data1 = [t for t in data if t]
print(data1)

# 23. Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(price, key=lambda x: float(x[1]), reverse=True))

# 24. Write a Python program to count the elements in a list until an element is a tuple.

num = [10, 20, 30, (10, 20), 40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)
