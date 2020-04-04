# File Objects
import os
os.chdir('/Users/Praful/Desktop/python/File-Objects/')
f = open('test.txt', 'r')
print(f.name)
print(f.mode)
f.close()

with open('test.txt', 'r') as f:
    # f_contents = f.read()
    f_contents = f.readline()
    # f_contents = f.readlines()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents)

print(f.closed)

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end="")

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents, end='')

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='*')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())
while len(f_contents) > 0:
    print(f_contents, end='*')
    f_contents = f.read(size_to_read)

with open('test2.txt', 'w') as f:
    f.write('Test')

with open('test2.txt', 'w') as f:
    pass

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('img.jpg', 'r') as rf:
    with open('code.jpg', 'w') as wf:
        for line in rf:
            w.write(line)

with open('img.jpg', 'r') as rf:
    with open('code.jpg', 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
