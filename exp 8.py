Implement ‘re’ module in python
Aim
To implement the re module in Python for pattern matching and text searching.
Algorithm
Start the program
Import the re module
Define a string
Use re.search() to find a pattern
Use re.match() to match from beginning
Use re.findall() to find all matches
Display the results
Stop the program

#code
import re

# Sample string
text = "My phone number is 9876543210 and email is test123@gmail.com"

# 1. Search for a number
pattern1 = r'\d{10}'
result1 = re.search(pattern1, text)

if result1:
    print("Phone Number Found:", result1.group())

# 2. Match (checks only at beginning)
pattern2 = r'My'
result2 = re.match(pattern2, text)

if result2:
    print("Match Found at Beginning")

# 3. Find all digits
pattern3 = r'\d'
result3 = re.findall(pattern3, text)
print("All digits:", result3)

# 4. Find email
pattern4 = r'\S+@\S+'
result4 = re.search(pattern4, text)

if result4:
    print("Email Found:", result4.group())
