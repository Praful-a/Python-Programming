# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

# random tuple
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# element 'e' is searched
index = vowels.index('e')

# index is printed
print('The index of e:', index)

# element 'i' is searched
index = vowels.index('i')

# only the first index of the element is printed
print('The index of i:', index)
