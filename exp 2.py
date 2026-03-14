Write a Python program to demonstrate control flow statements and looping statements
Aim:
To write a Python program to demonstrate control statements such as if-else, for loop, and while loop in Python
Algorithm
step 1 :Start the program.
step 2 :Enter a number from the user.
step 3 :Use if-else to check whether the number is even or odd.
step 4 :Use a for loop to print numbers from 1 to 5.
step 5 :Use a while loop to print numbers from 1 to 5.
step 6 :Display the results.
step 6 :Stop 
# Experiment 2: Control Flow and Looping Statements
# Control Flow (if-else)
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# For Loop
print("Numbers using for loop:")
for i in range(1, 6):
    print(i)

# While Loop
print("Numbers using while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1
