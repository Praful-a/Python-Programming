import antigravity
import os
import calendar
import datetime
import math
import random
import sys
# Adding the dir if your file in other dir whatever you are importing you can save it like this below.
# sys.path.append('/Users/praful/Desktop/exercise.py')
# after add this line in your code then you need to set the path so you can set it just like you set you pathon setup path means you need to set this dir in you syster invornment by using the name PYTHONPATH

from exercise import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path)


courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)
print(random_course)


courses = ['History', 'Math', 'Physics', 'CompSci']

rads = math.radians(90)
print(math.sin(rads))


today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)
