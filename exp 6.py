Write a Python program to count the number of uppercase and lowercase characters in a string.
Aim:
To write a Python program to count the number of uppercase and lowercase characters in a string.
Algorithm
Step 1: Start the program.
Step 2: Read a string from the user.
Step 3: Initialize two variables upper and lower to 0.
Step 4: Traverse each character in the string using a loop.
Step 5: Check if the character is uppercase using isupper() and increase the counter.
Step 6: Check if the character is lowercase using islower() and increase the counter.
Step 7: Display the number of uppercase and lowercase characters.
Step 8: Stop the program.

#code
s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
  
