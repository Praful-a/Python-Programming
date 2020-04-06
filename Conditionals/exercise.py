# Conditions

if True:
    print('Conditional was True')

if false:
    print('Conditional was True')

language = 'Python'

if language == 'Python':
    print('Conditionals was True')

language = 'Java'

if language == 'Python':
    print('language is Python')
if language == 'Python':
    print('language is Python')
if language == 'Java':
    print('language is Java')

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a == b)
print(a is b)

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a == b)
print(a is b)

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 10

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


#take temp of water
temperature = int(input())
if temperature > 100:
    print('Steam')
elif temperature < 0:
    print('Ice')
else:
    print('Water')
