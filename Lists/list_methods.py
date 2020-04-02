# # You can learn more :- https://www.programiz.com/python-programming/methods/list

# append :- The append() method adds an item to the end of the list.
animals = ['cat', 'dog', 'rabbit']

animals.append('guinea pig')

print(animals)

extend: - The extend() extends the list by adding all items of a list(passed as an argument) to the end.

# language list
language = ['French', 'English', 'German']

# another list of language
language1 = ['Spanish', 'Portuguese']

language.extend(language1)

# Extended List
print('Language List: ', language)

# language list
language = ['French', 'English', 'German']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending element of language tuple
language.extend(language_tuple)

print('New Language List: ', language)

# appending element of language set
language.extend(language_set)

print('Newest Language List: ', language)

insert: - The insert() method inserts an element to the list at a given index.

# vowel list
vowel = ['a', 'e', 'i', 'u']

# inserting element to list at 4th position
vowel.insert(3, 'o')

print('Updated List: ', vowel)

mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List: ', mixed_list)

remove: - The remove() method removes the first matching element(which is passed as an argument) from the list.

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals)

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e'
index = vowels.index('e')
print('The index of e:', index)

# index of the first 'i'
index = vowels.index('i')
print('The index of i:', index)

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# 'p' doesn't exist in the list
index = vowels.index('p')
print('The index of p:', index)

# random list
random = ['a', ('a', 'b'), [3, 4]]

# index of ('a', 'b')
index = random.index(('a', 'b'))
print("The index of ('a', 'b'):", index)

# index of [3, 4]
index = random.index([3, 4])
print("The index of [3, 4]:", index)

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)

# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("The count of [3, 4] is:", count)

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:')
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)

# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)

old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)
