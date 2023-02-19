# decorators in python 
# decorators are used to add functionality to an existing code without modifying it.

# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function


# @decorator_function
# def display():
#     print('display function ran')

# display()



"""
In Python, a decorator is a function that takes another function as input and returns a new function as output. 
The new function returned by the decorator is typically a modified version of the original function. 
Decorators provide a way to modify the behavior of a function without changing its source code.

Here's an example of a simple decorator in Python:


"""
# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# @my_decorator
# def blabla():
#     print("blabla")    

# say_hello()
# blabla()
"""
In this example, my_decorator is a function that takes another function, func, as input.
The wrapper function is defined inside my_decorator and is returned as the new function.

The @my_decorator syntax is used to apply the my_decorator decorator to the say_hello function. 
When the say_hello function is called, the modified version of the function returned by the decorator is executed.

In this case, the modified version of the say_hello function prints "Before the function is called."
before executing the original say_hello function, and then prints "After the function is called."
after the original function has finished executing.

Decorators can be used for a wide range of purposes, such as:

    Adding functionality to a function, such as logging, timing, or caching.
    Restricting access to a function based on user authentication or authorization.
    Modifying the behavior of a function based on its inputs or outputs.
    Applying a consistent interface to a group of related functions.

"""

"""time delay decorator """
import time

def delay_decorator(function):
    def wrapper_function():
        """code goes here"""
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")







