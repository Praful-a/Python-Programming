def hello_func():
    pass


print(hello_func())


def hello_func():
    print('Hello function')


hello_func()

Keep your code DRY


def hello_func():
    print('Hello function!')


hello_func()
hello_func()
hello_func()
hello_func()


def hello_func():
    return 'Hello function!'


print(hello_func())
print(hello_func().upper())
print(len(hello_func()))


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hii', name="praful"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
student_info(*courses, **info)
