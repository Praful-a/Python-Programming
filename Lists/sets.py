# Sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
# print('Math' in cs_courses)
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Creating empty Sets

empty_set = {}  # This isn't right: It's a dict
empty_set = set()
