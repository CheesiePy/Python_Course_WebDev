#    Printing numbers 1 to 10 using a for loop:



for i in range(1, 11):
    print(i)

#    Calculating the sum of numbers 1 to 100 using a for loop:



sum = 0
for i in range(1, 101):
    sum += i
print("The sum is", sum)

#    Printing all even numbers from 1 to 20 using a for loop:


for i in range(2, 21, 2):
    print(i)

#    Printing the multiplication table of a given number using a for loop:

n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#    Printing the elements of a list using a for loop:


fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


# Harder Q'z

# Printing the first n fibonacci numbers using a for loop:


n = 10
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1]+fib[i-2])
print(fib[:n])

# Printing the prime numbers between a given range using a for loop:



def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

start = 10
end = 30
for i in range(start, end+1):
    if is_prime(i):
        print(i)

#Printing the elements of a nested list using a for loop:


numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lst in numbers:
    for num in lst:
        print(num, end=' ')
    print()
#Flattening a nested list using a for loop:


numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []
for lst in numbers:
    for num in lst:
        flat_list.append(num)
print(flat_list)


#Printing the frequency of each element in a list using a for loop:


numbers = [1, 2, 3, 4, 2, 1, 4, 4, 5, 1]
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

