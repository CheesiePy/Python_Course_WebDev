user_input = input("Enter a sentence: ")
output = ''
for i in user_input:
    if i == ' ':
        output += '\n'
    else:
        output += i
print(output)


