from datetime import datetime
import os

print(dir(os))
print(os.getcwd())
Changing the directory
os.chdir('/Users/Praful/Desktop/')
print(os.getcwd())

Creating folders
os.mkdir('OS-Demo-2')
os.makedirs('OS-Demo-2/Sub-Dir-1')

os.rmdir('OS-Demo-2')
os.removedirs('OS-Demo-2/Sub-Dir-1')

os.rename('test.txt', 'demo.txt')
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print(os.listdir())

for dirpath, dirnames, filename in os.walk('/Users/Praful/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filename)

print(os.environ.get('PATH'))
file_path = os.path.join(os.environ.get('PATH', 'test.txt'))
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
