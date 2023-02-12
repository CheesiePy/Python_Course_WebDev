condition = True

# if statement
if condition:
    print("condition is true")
    print("this will always happen")
    if 5 < 3:
        print("shlom")
    print("banana")

# if else statement
if condition:
    print("condition is true")
else:
    print("condition is false")

# if elif else statement`
if condition:
    print("condition is true")
elif 5 < 3:
    print("5 < 3")
else:
    print("condition is false")

# nested if statement
if condition:
    print("condition is true")
    if 5 < 3:
        print("shlom")
    print("banana")


# match statement
variable = 6
match variable:
    case 1:
        print("variable is 1")
    case 2:
        print("variable is 2")
    case 3:
        print("variable is 3")
    case _:
        print("variable is not 1, 2 or 3")

# # ternary operator
print("condition is true") if condition else print("condition is false")


