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


def rplc_vow(mystr):
    vowels='aeiouAEIOU'
    mylist = []
    for i in mystr:
        if i not in vowels:
            mylist.append(i)
        else:
            mylist.append("x")

    return "".join(mylist)

print(rplc_vow("pokemon"))





def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def alternate_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
    return result



def count_characters(string, char):
    return string.count(char)

def fibonacci(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def largest_number(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max

def sum_even(numbers):
    sum = 0
    for i in numbers:
        if i%2 == 0:
            sum += i
    return sum


def repeat_str(mystr, strnum):
    return mystr*int(strnum)

def remove_dup(list1):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    return result

def remove_dup_set(list1):
    return list(set(list1))        

l1 = [1,2,1,4,5,2,3,1]
print(remove_dup_set(l1))
print(remove_dup(l1))    