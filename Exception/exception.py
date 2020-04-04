import os
os.chdir('/Users/Praful/Desktop/python/Exception/')
# try:
#     f = open('testfile.txt')
# except Exception:
#     print('Sorry. This file does not exist')

# try:
#     f = open('test_file.txt')
#     var = bad_var
# except SyntaxError:
#     print('Sorry. This file does not exist')
# except Exception:
#     print('Sorry. Something went wrong')

try:
    f = open('currupt_file.txt', 'r')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except SyntaxError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing the finally...')
