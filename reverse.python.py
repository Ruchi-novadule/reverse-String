user_input = input("Enter a string: ")

reversed_string = ""
index = len(user_input) - 1

while index >= 0:
    reversed_string += user_input[index]
    index -= 1

print("Reversed string is:", reversed_string)