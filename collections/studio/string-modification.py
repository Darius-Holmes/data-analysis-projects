my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

print(len(my_string))

my_string_slice = my_string[:3]
print(my_string_slice)

part_string = my_string[3:]
print(part_string)

new_string = part_string+my_string_slice

print(new_string)

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"The first string was {my_string} and the new string is {new_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

user_input = int(input('Enter number of letters to relocate: '))


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

if user_input > len(my_string):
    print(f"The input {user_input} exceeds string length. Will default to 3")
    user_input = 3

my_string_slice = my_string[:user_input]
part_string = my_string[user_input:]
new_string = part_string + my_string_slice


print(new_string)