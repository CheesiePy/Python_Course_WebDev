"""
Write a function that takes a string as input and returns a string with all vowels removed.

Write a function that takes a number as input and returns its factorial.

Write a function that takes two lists of equal length as input and returns a new list containing the elements of both lists, alternating between the two.

Write a function that takes a string as input and returns the number of times a specific character appears in the string.

Write a function that takes a number as input and returns its Fibonacci sequence up to that number.

Write a function that takes a list of numbers as input and returns the largest number in the list.

Write a function that takes a string as input and returns a string with all vowels replaced with 'x'.

Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.

Write a function that takes two strings as input and returns a string with the first string repeated the number of times specified by the second string.

Write a function that takes a list of numbers as input and returns a new list with all duplicates removed

"""

def rem_vow(mystr):
    vowels='aeiouAEIOU'
    mylist = []
    for i in mystr:
        if i not in vowels:
            mylist.append(i)
    return "".join(mylist)

print(rem_vow("pokemon"))