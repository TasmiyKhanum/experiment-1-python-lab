Write a Python program to perform string operations.
Algorithm
Step 1: Start the program.
Step 2: Read a string from the user.
Step 3: Find the length of the string using len() function.
Step 4: Convert the string to uppercase.
Step 5: Convert the string to lowercase.
Step 6: Perform string concatenation.
Step 7: Display a substring using slicing.
Step 8: Stop the program.

code 
s = input("Enter a string: ")

# Length of string
print("Length of string:", len(s))

# Uppercase
print("Uppercase:", s.upper())

# Lowercase
print("Lowercase:", s.lower())

# Concatenation
s2 = " Python"
print("Concatenation:", s + s2)

# String slicing
print("First 3 characters:", s[0:3])
