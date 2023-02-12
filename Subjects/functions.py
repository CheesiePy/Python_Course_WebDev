# Functions In Python


# function definition

def f():
    print("f")

# function with arguments
def g(a):
    print(f'g({a})')


def h(a, b):
    print(f'h({a}, {b})')


# function with default arguments
def c(a=1, b=2):
    print(f'c({a}, {b})')


# function with variable number of arguments
# *args is a tuple of arguments passed to the function 
def d(*args):
    print(f'd({args})')


# return value from function

def e():
    return 1

x = e()

# recursive function
def fr():
    print("f")
    f() # this will cause an error

# basic exit condition for recursive function

def fr1(counter):
    if counter == 0:
        return
    print("f")
    fr1(counter - 1)

# recursive functions example
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


