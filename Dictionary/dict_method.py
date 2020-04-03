d = {'name': 'John', 'age': 23, 'phone': '23232323'}
d.clear()
print(d)

d = {'name': 'John', 'age': 23, 'phone': '23232323'}
a = d.copy()
print(a)
# or
b = d
print(b)

keys = {'a', 'e', 'i', 'o', 'u'}

vowels = dict.fromkeys(keys)
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

vowels = {key: list(value) for key in keys}
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)

person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.items())

sales = {'apple': 2, 'orange': 3, 'grapes': 4}

items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())

person = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

result = person.popitem()
print('person = ', person)
print('Return Value = ', result)

person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ', person)
print('Age = ', age)

person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ', person)
print('salary = ', salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ', person)
print('age = ', age)

sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)

sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('guava')

sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.values())

sales = {'apple': 2, 'orange': 3, 'grapes': 4}

values = sales.values()
print('Original items:', values)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', values)

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

d = {'x': 2}

d.update(y=3, z=0)
print(d)
