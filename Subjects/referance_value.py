## mutable...
z = "Python"
x = [1,2,3]
y = [1,2,3]
w = "Python"

print(z is w)


print(x is y)


# def f(a): # mutator 
#     a.append(5)

# f(y) ### a = y

print(x == y) # True






# print(x)
# for i in range(1):
#     print("memory storage for x:",hex(id(x)))
#     print("memory storage for y:",hex(id(y)))

# for i in x:
#     print(f'memory storage for {i}:',hex(id(i)))

# # imutable 
# x[0] = 2
# x[2] = 2
# for i in range(1):
#     print("memory storage for x:",hex(id(x)))
#     print("memory storage for y:",hex(id(y)))

# for i in x:
#     print(f'memory storage for {i}:',hex(id(i)))

# print(x)

# x = 1

# x = 2