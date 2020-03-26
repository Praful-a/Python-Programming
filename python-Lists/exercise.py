# # Here we are working with lists. Lists is a mutable data type in python there are some built in function in list you can see any function description with help of help funciton like
# help(list.append).

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
# To check the length of our list we can use len function in python.
print(len(courses))

Index in python. indexing starts from 0 by default.
print(courses[0])
# Output History

print(courses[3])

Negative indexes
print(courses[-1])

# Slicing in python
print(courses[0:2])

# we get the same result because there are three steps in slicing (start, stop, step) and start by default 0.
print(courses[:2])
print(courses[2:])


courses.append('Art')

print(courses)

courses.insert(0, 'Art')
print(courses)

courses2 = ['Art', 'Education']
courses.insert(0, courses2)
print(courses)
print(courses[0])

courses.extend(courses2)
print(courses)

courses.remove('Math')
print(courses)

courses.pop()
print(courses)

popped = courses.pop()
print(popped)


courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 4, 2, 3]

print(min(nums))

print(max(nums))
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

sorted_courses = sorted(courses)
print(sorted_courses)

print(courses.index('CompSci'))
print('Art' in courses)
print('Math' in courses)

for index, item in enumerate(courses, start=1):
    print(index, item)

course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

# Creating empty list

empty_list = []
empty_list = list()
