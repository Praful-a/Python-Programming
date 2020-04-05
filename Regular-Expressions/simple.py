import re
import os
os.chdir('/Users/Praful/Desktop/python/Regular-Expressions/')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'Start')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'dne')
# pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)

# matches = pattern.match(sentence)
matches = pattern.search(sentence)

print(matches)

# for match in matches:
#     print(match)


emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#
# matches = pattern.finditer(emails)
#
# for match in matches:
#     print(match)


# print(r'\tTab')

# pattern = re.compile(r'abc')
# pattern = re.compile(r'cba')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'.')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')

# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'a$')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]')
# pattern = re.compile(r'[^b]at')

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'Mr\.')
# pattern = re.compile(r'Mr\.?')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
#
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)


# print(text_to_search[1:4])


# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)
