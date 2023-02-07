# Create a list of the squares of numbers from 1 to 10 using a list comprehension.
squared_numbers = [x**2 for x in range(1, 11)]

# Create a list of numbers from 1 to 10 that are divisible by 3 using a list comprehension.

d3_list = [x for x in range(1,11) if x % 3 == 0]

# Create a list of the first 10 even numbers using a list comprehension.

even_numbers = [x for x in range(2, 21, 2)]

# Create a list of all the uppercase letters in the string "Hello, World!" using a list comprehension.

uppercase_letters = [char for char in "Hello, World!" if char.isupper()]

# Create a list of the lengths of the words in the string "The quick brown fox jumps over the lazy dog" using a list comprehension

word_lengths = [len(word) for word in "The quick brown fox jumps over the lazy dog".split()]


# Create a list of the squares of even numbers from 1 to 10 using a list comprehension.

squared_even_numbers = [x**2 for x in range(2, 11, 2)]


# Create a list of all the vowels in the string "Hello, World!" using a list comprehension.

vowels = [char for char in "Hello, World!" if char in "aeiouAEIOU"]


# Create a list of the sum of the elements in each tuple in the list [(1, 2), (3, 4), (5, 6)] using a list comprehension.

sums = [sum(tuple) for tuple in [(1, 2), (3, 4), (5, 6)]]


# Create a list of the first 10 Fibonacci numbers using a list comprehension.

fibonacci = [0, 1] 

[fibonacci.append(fibonacci[i-1] + fibonacci[i-2]) for i in range(2, 10)]

print(fibonacci)

# Create a list of all the numbers from 1 to 10 that are not divisible by 2 or 3 using a list comprehension.

not_divisible = [x for x in range(1, 11) if x % 2 != 0 and x % 3 != 0]