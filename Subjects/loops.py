# for loops

# range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# len() - returns the length of an object.

word = "hello word"
length = len(word)
print(length)

for i in range(length):
    print(word[i], i)


for char in word:
    print(char)

# for index in range(5):
#     print(index)

#[Q1] sum all digit of n.
# n = input("please enter n-digit number: ")

if 5 > 2:
    print("never gonna happend")
    print("this will always happen")
    if 5 < 3:
        print("shlom")
    print("banana")


# while loops 
word = "Hello Python"
index = 0
while index < len(word):
    print("index:", index)
    index += 1

"""
while <condition is True>:
    <do this code>
    
"""

"""
we can use break to break the loop 

while <condition is True>:
    <do this code>
    if <condition is True>:
        break - break the loop

and we can use continue to return to the top of the loop 

while <condition is True>:
    <do this code>
    if <condition is True>:
        continue - return to the top of the loop
"""

