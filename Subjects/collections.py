# list

# list is a collection which is ordered and changeable. Allows duplicate members.

# Create list
mylist = []
mylist = list()

# Access list
mylist = [1, 2, 3, 4, 5]
print(mylist[0]) # 1

# Change list
mylist = [1, 2, 3, 4, 5]
mylist[0] = 10

# Loop list
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    print(i)

# Check if item exists
mylist = [1, 2, 3, 4, 5]
if 1 in mylist:
    print("yes")

# List length
mylist = [1, 2, 3, 4, 5]
print(len(mylist))

# Add item
mylist = [1, 2, 3, 4, 5]
mylist.append(6)

# Remove item
mylist = [1, 2, 3, 4, 5]
mylist.remove(1)

# Remove item by index
mylist = [1, 2, 3, 4, 5]
mylist.pop(0)

# Remove last item
mylist = [1, 2, 3, 4, 5]
mylist.pop()

# Remove all items
mylist = [1, 2, 3, 4, 5]
mylist.clear()



# tuple

# tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
mytuple = ()
mytuple = tuple()

# Access tuple
mytuple = (1, 2, 3, 4, 5)
print(mytuple[0]) # 1

# Loop tuple
mytuple = (1, 2, 3, 4, 5)
for i in mytuple:
    print(i)

# Check if item exists
mytuple = (1, 2, 3, 4, 5)
if 1 in mytuple:
    print("yes")

# Tuple length
mytuple = (1, 2, 3, 4, 5)
print(len(mytuple))

# Add item
mytuple = (1, 2, 3, 4, 5)
# mytuple.append(6) # error
# tuple does not support item assignment
# mytuple[0] = 10 # error



# set

# set is a collection which is unordered and unindexed. No duplicate members.

# Create set
myset = {}
myset = set()

# Access set
myset = {1, 2, 3, 4, 5}
# print(myset[0]) # error

# Loop set
myset = {1, 2, 3, 4, 5}
for i in myset:
    print(i)

# Check if item exists
myset = {1, 2, 3, 4, 5}
if 1 in myset:
    print("yes")

# Set length
myset = {1, 2, 3, 4, 5}
print(len(myset))

# Add item
myset = {1, 2, 3, 4, 5}
myset.add(6)

# Remove item
myset = {1, 2, 3, 4, 5}
myset.remove(1)

# Remove last item
myset = {1, 2, 3, 4, 5}
# myset.pop() # error

# Remove all items
myset = {1, 2, 3, 4, 5}
myset.clear()

# Join sets
myset1 = {1, 2, 3, 4, 5}
myset2 = {6, 7, 8, 9, 10}
myset3 = myset1.union(myset2)
myset4 = myset1.intersection(myset2)

# Remove duplicates
mylist = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# myset = set(mylist)
# mylist = list(myset)
mylist = list(set(mylist))





# dictionary

# dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# dictionary is a collection of key-value pairs.

# Create dictionary

mydict = {}
mydict = dict()

# Access dictionary
mydict = {"name": "John", "age": 36}
print(mydict["name"]) # John

# Change dictionary
mydict = {"name": "John", "age": 36}
mydict["name"] = "Jane"

# Loop dictionary
mydict = {"name": "John", "age": 36}
for i in mydict:
    print(i) # name, age

# Loop dictionary values
mydict = {"name": "John", "age": 36}
for i in mydict:
    print(mydict[i]) # John, 36

# Loop dictionary values
mydict = {"name": "John", "age": 36}
for i in mydict.values():
    print(i) # John, 36

# Loop dictionary keys
mydict = {"name": "John", "age": 36}
for i in mydict.keys():
    print(i) # name, age

# Loop dictionary items
mydict = {"name": "John", "age": 36}
for i, j in mydict.items():
    print(i, j) # name John, age 36

# Check if key exists
mydict = {"name": "John", "age": 36}
if "name" in mydict:
    print("yes")

# Dictionary length
mydict = {"name": "John", "age": 36}
print(len(mydict))

# Add item
mydict = {"name": "John", "age": 36}
mydict["address"] = "Highway 37"

# Remove item
mydict = {"name": "John", "age": 36}
mydict.pop("name")

# Remove last item
mydict = {"name": "John", "age": 36}
# mydict.popitem() # error

# Remove all items
mydict = {"name": "John", "age": 36}
mydict.clear()

# Copy dictionary
mydict1 = {"name": "John", "age": 36}
mydict2 = mydict1.copy()

# Nested dictionary
mydict = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
}










mydict = {}
myset = set()

