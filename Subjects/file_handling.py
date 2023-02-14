# files in python

# open a file
f = open('test.txt', 'r')

# read the file
print(f.read())

# close the file
f.close()


# open second parameter is the mode
# r - read
# w - write
# a - append
# r+ - read and write

# read a file line by line
f = open('test.txt', 'r')
for line in f:
    print(line)

# close the file
f.close()


# write to a file
f = open('test.txt', 'w')
f.write('This is a test')
f.close()


# append to a file
f = open('test.txt', 'a')
f.write('This is a test')
f.close()

# read and write to a file
f = open('test.txt', 'r+')
f.write('This is a test')
f.close()

# its better to use the with statement
# this will automatically close the file
with open('test.txt', 'r') as f:
    print(f.read())

# read a file line by line
with open('test.txt', 'r') as f:
    for line in f:
        print(line)

# write to a file
with open('test.txt', 'w') as f:
    f.write('This is a test')

# append to a file
with open('test.txt', 'a') as f:
    f.write('This is a test')

# read and write to a file
with open('test.txt', 'r+') as f:
    f.write('This is a test')
    x = f.read()
    print(x)


# we catch the exception if the file does not exist
try:
    f = open('test.txt', 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('File not found')

# we can also use the with statement
try:
    with open('test.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('File not found')




