# write a lambda function that takes a number and returns its square

# write a map function that squares a list of numbers

# write a filter function that returns only the even numbers from a list of numbers

# write a reduce function that returns the sum of the squars of a list of number
from functools import reduce

def f(x,y):
    return x**2 + y**2

l = [0,1,2,3,4]

sl = reduce(f,l)

print(sl)

# write a lambda function that takes two string and return it concatenated like this 'Hello World Hello'

magic = lambda x,y: f'{x} {y} {x}'
print(magic("Hello", "World"))