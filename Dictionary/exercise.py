student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# print(student)
# print(student['name'])
# print(student['courses'])
# student['phone'] = '555-5555'
# student['name'] = 'Jane'
#
# print(student.get('name'))
#
# print(student.get('phone', 'Not found'))

# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

# del student['age']
# age = student.pop('age')
#
# print(student)
# print(age)

# print(len(student))
# print(student.keys())
# print(student.items())
# print(student.values())

# for key in student:
#     print(key)

for key, value in student.items():
    print(key, value)
