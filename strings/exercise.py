
message = "Bobby's world"
print(message)

# or you can do this and get the same answer
message2 = 'Bobby\'s world'
print(message2)

# multiple line string
message3 = """Bobby is a good boy.
He is 12 years old."""
print(message3)

length function
message4 = 'Hello world'
print(len(message4))

Indexing
mes = 'Hello world'
print(mes[10])
print(mes[7])

# slicing
mes2 = 'Hello world'
print(mes2[0:5])
# or
print(mes2[:5])
print(mes2[6:])

# #######################
# Methods
# #######################
# You can read more from this link: https://www.programiz.com/python-programming/methods/string


mes = 'Hello World'
print(mes.lower())

mes = 'Hello World'
print(mes.upper())

mes2 = 'Hello World'
print(mes2.count('l'))

mes3 = 'Hello World'
print(mes3.find('World'))

mes4 = 'Hello World'
This won't be work
mes4.replace('World', 'Universe')
new_mes = mes4.replace('World', 'Universe')
print(new_mes)

greeting = 'Hello'
name = 'Micheal'

mes = greeting + ', ' + name + '. Welcome!'
print(mes)

# Other way
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# using 'f' string
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# see all string methods
print(dir(str))

# If you want help
print(help(str.upper))

mes = 'hello world'
print(mes.capitalize())

string = "Python is awesome"
new_string = string.center(24, '@')
print(new_string)


similer as lower method
string = "PYTHON IS AWESOME"
print(string.casefold())

text = "Python is easy to learn."

result = text.endswith('to learn')
print(result)

result = text.endswith('to learn.')
print(result)

result = text.endswith('Python is easy to learn.')
print(result)

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched
result = text.endswith('is', 7, 26)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)

# Passing tuple suffix in endswith
text = "programming is easy"
result = text.endswith(('programming', 'python'))
print(result)

restul = text.endswith(('python', 'easy', 'java'))
print(result)

result = text.endswith(('is', 'an'), 0, 14)
print(result)

str = 'xyx\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()
print(result)

str = 'xyx\t12345\tabc'

# tabsize is set to 2
print(str.expandtabs(2))

# tabsize is set to 3
print(str.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', str.expandtabs(6))

text = "Python is easy to learn."

result = text.startswith('is easy')
print(result)

result = text.startswith('Python is ')
print(result)

result = text.startswith('Python is easy to learn.')
print(result)

text = "Python programming is easy."

# start parameter: 7
# 'programming is easy.' string is searched
result = text.startswith('programming is', 7)
print(result)

# start: 7, end: 18
# 'programming' string is searched
result = text.startswith('programming is', 7, 18)
print(result)

result = text.startswith('program', 7, 18)
print(result)

# startswith() with Tuple Prefix
text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)

grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())

text = 'Love thy neighbor'

# splits at space
print(text.rsplit())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.rsplit(', '))

# Splitting at ':'
print(grocery.rsplit(':'))

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.rsplit(', ', 2))

# maxsplit: 1
print(grocery.rsplit(', ', 1))

# maxsplit: 5
print(grocery.rsplit(', ', 5))

# maxsplit: 0
print(grocery.rsplit(', ', 0))

text = 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splitting at ':'
print(grocery.split(':'))

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))

quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)

result = quote.rindex('small')
print("Substring 'small ':", result)

quote = 'Do small things with great love'

# Substring is searched in ' small things with great love'
print(quote.rindex('t', 2))

# Substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))

# Substring is searched in 'hings with great lov'
print(quote.rindex('o small ', 10, -1))

quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if (result != -1):
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contain substring")

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))

# translation table - a dictionary
translation = {97: None, 98: None, 99: 105}

string = "abcdef"
print("Original string:", string)

# translate string
print("Translated string:", string.translate(translation))

string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is '))

# 'not' separator is not found
print(string.rpartition('not '))

string = "Python is fun, isn't it"

# splits at last occurence of 'is'
print(string.rpartition('is'))

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

quote = 'Let it be, let it be, let it be'

result = quote.find('let it')
print("Substring 'let it':", result)

result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())

s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())

str = 'Python'
print(str.isidentifier())

str = 'Py thon'
print(str.isidentifier())

str = '22Python'
print(str.isidentifier())

str = ''
print(str.isidentifier())

s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

s = '1242323'
print(s.isnumeric())

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())

# s = '½'
s = '\u00BD'
print(s.isnumeric())

s = '1242323'
s = 'python12'
print(s.isnumeric())

s = 'Space is a printable'
print(s)
print(s.isprintable())

s = '\nNew Line is printable'
print(s)
print(s.isprintable())

s = ''
print('\nEmpty string printable?', s.isprintable())

numList = ['1', '2', '3', '4']
seperator = ', '
print(seperator.join(numList))

numTuple = ('1', '2', '3', '4')
print(seperator.join(numTuple))

s1 = 'abc'
s2 = '123'

""" Each character of s2 is concatenated to the front of s1"""
print('s1.join(s2):', s1.join(s2))

""" Each character of s1 is concatenated to the front of s2"""
print('s2.join(s1):', s2.join(s1))

test = {'2', '1', '3'}
s = ', '
print(s.join(test))

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

test = {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test = {1: 'mat', 2: 'that'}
s = ', '

# this gives error
print(s.join(test))

# example string
string = 'cat'
width = 5

# print left justified string
print(string.ljust(width))

# example string
string = 'cat'
width = 5
fillchar = '*'

# print left justified string
print(string.ljust(width, fillchar))

string = 'cat'
width = 5

# print right justified string
print(string.rjust(width))

# example string
string = 'cat'
width = 5
fillchar = '*'

# print right justified string
print(string.rjust(width, fillchar))

# example string
string = "THIS SHOULD ALL BE LOWERCASE."
print(string.swapcase())

string = "this should all be uppercase."
print(string.swapcase())

string = "ThIs ShOuLd Be MiXeD cAsEd."
print(string.swapcase())

random_string = '   this is good '

# Leading whitepsace are removed
print(random_string.lstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))

print(random_string.lstrip('s ti'))

website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))

random_string = ' this is good'

# Leading whitepsace are removed
print(random_string.rstrip())

# Argument doesn't contain 'd'
# No characters are removed.
print(random_string.rstrip('si oo'))

print(random_string.rstrip('sid oo'))

website = 'www.programiz.com/'
print(website.rstrip('m/.'))

string = ' xoxo love xoxo   '

# Leading whitepsace are removed
print(string.strip())

print(string.strip(' xoxoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('sti'))

string = 'android is awesome'
print(string.strip('an'))

string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is'))

# example dictionary
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))

# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))

# example dictionary
firstString = "abc"
secondString = "defghi"
string = "abc"
print(string.maketrans(firstString, secondString))
