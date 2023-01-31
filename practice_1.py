# #    Printing numbers 1 to 10 using a for loop:

# # for i in range(1,11):
# #     print(i)

# #    Calculating the sum of numbers 1 to 100 using a for loop:
# import timeit

# t1 = timeit.default_timer()

# sum = 0
# for i in range(1010):
#     sum += i
# print(sum)

# t2 = timeit.default_timer()

# print("time in seconds:" , t2 - t1)

# nRows = 5

# for i in range(1,nRows+1):  #outer loop
#     for j in range(i): #inner loop
#         print("*", end = "")
#     print() 


# #    Printing all even numbers from 1 to 20 using a for loop:

# for i in range(1, 21):
#     if not i%2:
#         print(i)

# #    Printing the multiplication table of a given number using a for loop:
# import random
# n = random.randint(1, 10)
# for i in range(1, 11):
#     print(i ,"*", n, "=",i*n, end="|", sep="")
# print()

# #    Printing the elements of a list using a for loop:
# mylist = list(range(random.randint(1,50)))

# for i in range(len(mylist)):
#     print(mylist[i])


# for i in mylist:
#     print(i)

# print(mylist)




# Harder Q'z

# [Q1] Printing the first n fibonacci numbers using a for loop:

# [Q2] Printing the prime numbers between a given range using a for loop:

# [Q3] {fix the bugs!} Printing the elements of a nested list using a for loop:

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for lst in numbers:
#     for num in lst:
#     print(lst)

# #[Q4] { fix the bugs! } Flattening a nested list using a for loop:


# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = []:
#     for lst in numbers:
#         for num in lst{
# list.append(num)
#         }    
# print(FlatList);


# #[Q5] Printing the frequency of each element in a list using a for loop:


numbers = [1, 2, 3, 4, 2, 1, 4, 4, 5, 1]
freq = {}
for i in range(len(numbers)):
    if numbers[i] in freq:
        freq[numbers[i]] += 1
    else:
        freq[numbers[i]] = 1 
print(freq)

