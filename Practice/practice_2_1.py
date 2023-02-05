#     Write a program to convert the first letter of a string to uppercase.

text = "hello world"
print(text.capitalize())

#     Write a program to count the number of occurrences of a substring in a string.

print(text.count("world"))

#     Write a program to check if a string starts with a specific substring.

print(text.startswith("hello"))

#     Write a program to check if a string ends with a specific substring.

print(text.endswith("hello"))

#     Write a program to find the index of a substring in a string.

print(text.index("hello"))


#     Write a program to split a string into a list based on a specific character.

c = " "
print(text.split(c))

#     Write a program to replace a specific substring in a string.

text = text.replace("hello", "goodbye")
print(text)

#     Write a program to check if a string is alphanumeric.

user_input = input("Please Enter something: ")
if(user_input.isalnum()):
    print(user_input, "is alpha numeric")
else:
    print(user_input, "is not alpha numric")    


#     Write a program to check if a string is alphabetic.
if(user_input.isalpha()):
    print(user_input, "is alpha")
else:
    print(user_input, "is not alpha")    

#     Write a program to check if a string is numeric.
if(user_input.isnumeric()):
    print(user_input, "is numeric")
else:
    print(user_input,"is not numeric")

#     Write a program to check if a string is lowercase.
print(user_input.islower())
#     Write a program to check if a string is uppercase.
print(user_input.isupper())
#     Write a program to strip whitespace from the beginning and end of a string.

text = "          hello               my            "
print(text.strip())