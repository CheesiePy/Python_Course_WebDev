# for loops

# range() - returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# len() - returns the length of an object.

# word = "hello word"
# length = len(word)
# print(length)

# for i in range(length):
#     print(word[i], i)


# for char in word:
#     print(char)

# for index in range(5):
#     print(index)


# while loops 
# word = "Hello Python"
# index = 0
# while index < len(word):
#     print("index:", index)
#     index += 1

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
# example
flag = False
counter = 0
while not flag:
    counter += 1    
    if counter > 10:
        print(counter)
        flag = True
    

