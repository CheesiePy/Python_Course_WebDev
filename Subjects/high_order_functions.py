# high order functions in python

# function that takes another function as an argument
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

# function that returns another function
def make_adder(n):
    def adder(x):
        return x + n
    return adder

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(4))
print(plus_5(4))


# lambda functions

x = lambda x: x + 5
print(x(5)) # 10

# lambda functions are small anonymous functions

g = lambda x, y: "x is greater than y" if x > y else "y is greater than x"
print(g(5, 10)) # y is greater than x


# lambda functions can take any number of arguments, but can only have one expression
import time
t = lambda : time.time()
print(t()) 


# lambda functions are used along with built-in functions like filter(), map() and reduce()

# filter() function
# filter() function takes two arguments: a function and a list
# filter() function returns a list of elements for which the function returns true


def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(is_even, numbers))
print(evens) # [2, 4, 6, 8, 10]


# map() function
# map() function takes two arguments: a function and a list
# map() function returns a new list with the function applied to each element

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(square, numbers))

print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# reduce() function
# reduce() function takes two arguments: a function and a list
# reduce() function returns a single value
# functools module is required to use reduce() function
# functools module is part of the standard library in Python 3 but not in Python 2
# functools module helps to write functions that act on or return other functions

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(add, numbers)

print(sum) # 55


# lambda functions are used along with built-in functions like filter(), map() and reduce()

# filter() function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens) # [2, 4, 6, 8, 10]


# map() function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x * x, numbers))

print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# reduce() function

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x + y, numbers)

print(sum) # 55







