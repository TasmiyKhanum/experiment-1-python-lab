write a Python program to create and use functions with parameters.
Aim:
To write a Python program to create and use functions with parameters in Python.
Algorithm
Step 1: Start the program.
Step 2: Define a function to add two numbers.
Step 3: Read two numbers from the user.
Step 4: Call the function and pass the numbers as arguments.
Step 5: Store the returned result.
Step 6: Display the sum of the two numbers.
Step 7: Stop the program.

# 
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum =", result)
