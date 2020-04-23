# 1. Write a Python program to sum all the items in a list.


def sum_all_items(num):
    summ = 0
    for i in num:
        summ += i
    return summ


result = sum_all_items([1, 2, 3, 4, 5])
print(result)

# 2. Write a Python program to multiplies all the items in a list.


def multiply_all_items(num):
    mul = 1
    for i in num:
        mul *= i
    return mul


result = multiply_all_items([1, 2, 3, 4, 5])
print(result)

# 3. Write a Python program to get the largest number from a list.


def largest_num(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    return m


print(largest_num([10, 2, 3, 4, 5]))

# 4. Write a Python program to get the smallest number from a list.


def smallest_num(l):
    s = l[0]
    for i in l:
        if i < s:
            s = i
    return s


print(smallest_num([1, -1, -4, 3, 2, -2]))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.


def count_string(l):
    summ = 0
    for word in l:
        if len(word) > 1 and word[0] == word[-1]:
            summ += 1
    return summ


print(count_string(['xyz', 'abc', 'aba', 'aba', 'a', 'b']))

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
n = len(l):
for i in range(n):
    for j in range(1, n-i):
        if l[j-1][1] > l[j][1]:
            l[j-1], l[j] = l[j], l[j-1]
print(l)
or
def sort_list_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])


print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 7. Write a Python program to remove duplicates from a list.


def remove_deplicates(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res


print(remove_deplicates([1, 1, 2, 2, 3, 4, 5, 5, 6, 4, 2, 1]))

# 8. Write a Python program to check a list is empty or not.


def list_empty(l):
    if l:
        return 'List is not Empty'
    else:
        return 'List is empty'


print(list_empty([1]))

# 9. Write a Python program to clone or copy a list.


def copy_list(l):
    a = 0
    a = l
    return a


print(copy_list([1, 23, 4, 5]))

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.


def words(n, word):
    word_len = []
    for w in word.split(" "):
        if len(w) > n:
            word_len.append(w)
    return word_len


print(words(3, "The quick brown fox jumps over the lazy dog"))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.


def common_mem(l1, l2):
    result = False
    for i in l1:
        for j in l2:
            if i == j:
                result = True
        return result


print(common_mem([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.


def remove_list_items(l):
    res = []
    for i in range(len(l)):
        if i == 0 or i == 4 or i == 5:
            continue
        else:
            res.append(l[i])
    return res


print(remove_list_items([1, 2, 3, 4, 5, 6, 7]))

or
def remove_list_items(l):
    l1 = [v for i, v in enumerate(l) if i not in (0, 4, 5)]
    return l1


print(remove_list_items([1, 2, 3, 4, 5, 6, 7]))

13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
list1 = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(list1)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def remove_even_no(l):
    res = []
    for num in l:
        if num % 2 != 0:
            res.append(num)
    return res


print(remove_even_no([1, 2, 3, 4, 5, 6]))

# 15. Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
l = []
for i in range(1, 30):
    l.append(i**2)
print(l[1:6])
print(l[-5:-1])

# 18. Write a Python program to generate all permutations of a list in Python.
import itertools
l = itertools.permutations([1, 2, 3])
print(list(l))

# 19. Write a Python program to get the difference between the two lists.
l1 = [1, 2, 3, 4, 5]
l2 = [1, 4, 5, 7, 8]
print(list(set(l1) - set(l2)))

# 20. Write a Python program access the index of a list.
l = [1, 2, 3, 4, 5]
for i, v in enumerate(l):
    print(i, v)
