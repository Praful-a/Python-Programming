import os
os.chdir('/Users/Praful/Desktop/music')

# for f in os.listdir():
#     print(f)

# for f in os.listdir():
#     print(os.path.splitext(f))

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    # print(file_name)
    # print(file_name.split('-'))
    f_title, f_course, f_num = f_name.split('-')
    # print(f_title)
    # print(f_course)
    # print(f_num)
    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_num = f_num.strip()
    # removing the '#' tag
    # f_num = f_num.strip()[1:]
    # adding '0' in front of each digit
    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)
