# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
from collections import Counter
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: -2}
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(sorted_d)
sorted_d2 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_d2)

# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
d = {0: 10, 1: 20}
d[2] = 30
print(d)
# or
d.update({2: 30})
print(d)

# 3. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
# or
d4 = {}
for d in (dic1, dic2, dic3):
    d4.update(d)
print(d4)

# 4. Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def key_exists(k):
    for x in d.keys():
        if k == x:
            return "Key exists!"
        else:
            return "key does not exists!"


print(key_exists(1))
print(key_exists(8))

# 5. Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30}
for k, v in d.items():
    print(k, ' -> ', v)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def generate_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i*i
    return d


print(generate_dict(5))

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


def generate_d(n):
    d = {}
    for num in range(1, n+1):
        d[num] = num*num
    return d


print(generate_d(15))

# 10. Write a Python program to sum all the values of a dictionary.
d = {'x': 100, 'y': 200, 'z': 15}
print(sum(d.values()))

# 11. Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
m = 1
for v in my_dict.values():
    m *= v
print(m)

# 12. Write a Python program to remove a key from a dictionary.
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
if 'a' in myDict:
    del myDict['a']
print(myDict)

# 13. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
# print(dict(zip(keys, values)))
# or
d = {}
for k in keys:
    for v in values:
        d[k] = v
print(d)

# 14. Write a Python program to sort a dictionary by key.
color_dict = {'red': '#FF0000',
              'green': '#008000',
              'black': '#000000',
              'white': '#FFFFFF'}
for i in sorted(color_dict):
    print(i, color_dict[i])

# 15. Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {'x': 6000, 'y': 5874, 'z': 560}
m = my_dict['x']
for k, v in my_dict.items():
    if v > m:
        m = v
print(m)

m = my_dict['x']
for k, v in my_dict.items():
    if v < m:
        m = v
print(m)
# or
my_dict = {'x': 6000, 'y': 5874, 'z': 560}
key_max = max(my_dict.keys(), key=lambda k: my_dict[k])
key_min = min(my_dict.keys(), key=lambda k: my_dict[k])

print("Maximum value in dictionary: ", my_dict[key_max])
print("Minimum value in dictionary: ", my_dict[key_min])

# 16. Write a Python program to get a dictionary from an object's fields.


class Dict(object):
    def __init__(self):
        self.name = 'John'
        self.age = 22
        self.city = 'America'


test = Dict()
print(test.__dict__)

# 17. Write a Python program to remove duplicates from Dictionary.
student_data = {'id1':
                {'name': ['Sara'],
                 'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id2':
                {'name': ['David'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id3':
                {'name': ['Sara'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id4':
                {'name': ['Surya'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                }
d = {}
for key, value in student_data.items():
    if value not in d.values():
        d[key] = value
print(d)

# 18. Write a Python program to check a dictionary is empty or not.
d = {}
if d:
    print('Dictionary is not empty')
else:
    print('Dictionary is empty')

# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)

# 20. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print("Original List: ", L)
u_value = set(val for dic in L for val in dic.values())
print("Unique Values: ", u_value)
