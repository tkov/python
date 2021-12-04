import os

#print(dir(os))

print(os.getcwd()) # getting the current working directory 

os.chdir('..')

print(os.listdir()) # lists the files and folders in the current working directory

os.mkdir('dir1')
os.makedirs('dir2/dir3/dir4')

# remove directories
# os.rmdir()
# os.removedirs()

os.rename('test.txt', 'demo.txt') # rename : old, new

for dirpath, dirnames, filenames in os.walk(os.getcwd):
    print('Current Path', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()


print(os.path.exists('/tmp/test.txt'))


print(dir(os.path))

