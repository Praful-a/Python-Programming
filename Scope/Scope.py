'''
LEGB
Local, Enclosing, Global, Built-in
'''
# # x = 'global x'
#
#
# def test():
#     global x
#     x = 'local x'
#     # print(y)
#     print(x)
#
#
# test()
# print(x)

# x = 'global x'

# import builtins
#
# # print(dir(builtins))
#
#
# def my_min():
#     pass
#
#
# m = min([5, 1, 4, 2, 3])
# print(m)
#
#
# def test(z):
#     x = 'local x'
#     # print(y)
#     print(z)
#
#
# test('local z')


# def outer():
#     x = 'outer x'
#
#     def inner():
#         nonlocal x
#         x = 'inner x'
#         print(x)
#
#     inner()
#     print(x)
#
#
# outer()

x = 'global x'


def outer():
    # x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)
