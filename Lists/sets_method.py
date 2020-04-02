# # Learn more :- https://www.programiz.com/python-programming/methods/set

language = {'English', 'French', 'German'}

language.remove('German')

print(language)

# animal set
animal = {'cat', 'dog', 'rabbit', 'guinea pig'}

# Deleting 'fish' element
animal.remove('fish')

# Updated animal
print('Updated animal set: ', animal)

vowels = {'a', 'e', 'i', 'u'}
vowels.add('o')
print(vowels)

vowels.add('a')
print('Vowels are:', vowels)

# set of vowels
vowels = {'a', 'e', 'u'}

# a tuple ('i', 'o')
tup = ('i', 'o')

# adding tuple
vowels.add(tup)
print('Vowels are:', vowels)

# adding same tuple again
vowels.add(tup)
print('Vowels are:', vowels)

numbers = {1, 2, 3, 4}
new_num = numbers
new_num.add('5')

print(numbers)
print(new_num)

# set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
print('Vowels (before clear):', vowels)

# clearing vowels
vowels.clear()
print('Vowels (after clear):', vowels)

A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}

print(A.difference(B))
print(B.difference(A))
# or
print(A-B)
print(B-A)

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}

result = A.difference_update(B)
print('A = ', A)
print('B = ', B)
print('result = ', result)

number = {2, 3, 4, 5}
number.discard(3)
print('numbers = ', number)

number.discard(10)
print('number = ', number)

A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))

A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

print(A.intersection(D))
print(B.intersection(D))
print(C.intersection(D))
print(A.intersection(B, C, D))

A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3, 7}
D = {100, 200, 300}

print(A & C)
print(A & D)


print(A & C & D)
print(A & B & C & D)

result = A.intersection_update(B)

print('result =', result)
print('A =', A)
print('B =', B)

A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

result = C.intersection_update(B, A)

print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))

A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D = {1: 'a', 2: 'b'}
E = {'a': 1, 'b': 2}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))

A = {'a', 'b', 'c', 'd'}

print('Return Value is', A.pop())
print('A = ', A)

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}

print(A ^ B)
print(B ^ A)

print(A ^ A)
print(B ^ B)

A = {'a', 'c', 'd'}
B = {'c', 'd', 'e'}

result = A.symmetric_difference_update(B)

print('A =', A)
print('B =', B)
print('result =', result)
A = {'a', 'c', 'd'}
B = {'c', 'd', 2}
C = {1, 2, 3}

print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())

A = {'a', 'c', 'd'}
B = {'c', 'd', 2}
C = {1, 2, 3}

print('A U B =', A | B)
print('B U C =', B | C)
print('A U B U C =', A | B | C)

A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)

string_alphabet = 'abc'
numbers_set = {1, 2}

# add elements of the string to the set
numbers_set.update(string_alphabet)

print('numbers_set =', numbers_set)

info_dictionary = {'key': 1, 'lock': 2}
numbers_set = {'a', 'b'}

# add keys of dictionary to the set
numbers_set.update(info_dictionary)
print('numbers_set =', numbers_set)
