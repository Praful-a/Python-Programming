# 21. Write a Python program to convert a list of characters into a string.
from operator import itemgetter
from itertools import groupby
from itertools import zip_longest, chain, tee
from itertools import combinations
import random
import itertools
l1 = [1, 2, 3, 4, 5]
l2 = [str(i) for i in l1]
print(l2)

# 23. Write a Python program to flatten a shallow list.
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
new_list = []
for i in original_list:
    for j in i:
        new_list.append(j)
print(new_list)

#########################
# or
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
new_list = itertools.chain(*original_list)
print(list(new_list))

# 25. Write a Python program to select an item randomly from a list.
l = [1, 2, 3, 4, 5]
print(random.choice(l))

# 26. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# 27. Write a Python program to find the second smallest number in a list.
l = [1, 2, 3, 0, -2, -3]
l.sort()
print(l[1])
# or
mylist = [1, 2, 3, 0, -2, -3]
n = len(mylist)
for i in range(n):
    for j in range(1, n-i):
        if mylist[j-1] < mylist[j]:
            (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist[-2])


# 28. Write a Python program to find the second largest number in a list.
l = [1, 2, 3, 0, -2, -3]
l.sort()
print(l[-2])
# or
mylist = [5, 3, 7, 2, 8, 4]
n = len(mylist)
for i in range(n):
    for j in range(1, n-i):
        if mylist[j-1] > mylist[j]:
            (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist[-2])

# 30. Write a Python program to get the frequency of the elements in a list.
l = [1, 2, 2, 3, 3, 1, 5, 6, 7]
count = 1
d = {}
for i in l:
    if i not in d:
        d[i] = count
    else:
        d[i] += count
print(d)

# 31. Write a Python program to count the number of elements in a list within a specified range


def count_elements_in_list(min, max, l):
    ctr = 0
    for x in l:
        if min <= x <= max:
            ctr += 1
    return ctr


print(count_elements_in_list(0, 4, [0, 1, 2, 3, 4, 5, 6]))

# 32. Write a Python program to check whether a list contains a sublist.


def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True

    return sub_set


a = [2, 4, 3, 5, 7]
b = [4, 3]
c = []
print(is_Sublist(a, b))
print(is_Sublist(a, c))

# 33. Write a Python program to generate all sublists of a list.


def sub_lists(my_list):
    subs = []
    for i in range(1, len(my_list)+1):
        temp = [list(x) for x in combinations(my_list, i)]
        if len(temp) > 0:
            subs.extend(temp)
    return subs


l1 = [1, 2, 3]
print(sub_lists(l1))

# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.


def prime_eratosthenes(n):
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)


print(prime_eratosthenes(100))

or
lower = 1
upper = 10

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# 35-Demo. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
n = len(l)
for i in range(n):
    for j in range(0, n-i-1):
        if l[j][1] > l[j+1][1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)

# 36. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


def concate(l, n):
    new_list = []
    for i in range(1, n+1):
        for j in l:
            m = str(i)
            new_list.append(j+m)
    return new_list


print(concate(['p', 'q'], 5))

or
l = ['p', 'q']
new_list = []
for i in range(1, 5+1):
    for j in l:
        m = str(i)
        new_list.append(j+m)
print(new_list)

# 37. Write a Python program to find common items from two lists
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]


def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))


n = [0, 1, 2, 3, 4, 5]
print(replace2copy(n))3

# 39. Write a Python program to convert a list of multiple integers into a single integer.
l = [11, 22, 33]
l1 = [str(i) for i in l]
l1 = int(''.join(l1))
print(l1, type(l1))
or
l = [11, 22, 33]
k = int(''.join(map(str, l)))
print(k, type(k))

40. Write a Python program to split a list based on first character of word.

word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
