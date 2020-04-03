from operator import attrgetter
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)
print(s_li)
li.sort()
print(li)

s_li = sorted(li, reverse=True)
print(s_li)
li.sort(reverse=True)
print(li)

Tuple
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print(s_tup)

di = {'name': 'Corey', 'Job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print(s_di)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


def e_sort(emp):
    return emp.salary


s_emp = sorted(employees, key=e_sort)
print(s_emp)


s_emp = sorted(employees, key=lambda e: e.name)
print(s_emp)

s_emp = sorted(employees, key=attrgetter('age'))
print(s_emp)
