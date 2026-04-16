Write a program to implement numpy and pandas packages 
Aim

To implement and demonstrate the use of NumPy and Pandas packages in Python.
Algorithm
Start the program
Import numpy and pandas packages
Create a NumPy array
Perform basic operations (sum, mean)
Create a Pandas DataFrame
Display DataFrame and perform operations
Stop the program
#code 
# Importing libraries
import numpy as np
import pandas as pd

# -------- NUMPY IMPLEMENTATION --------
print("NUMPY OPERATIONS")

# Create array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))

# -------- PANDAS IMPLEMENTATION --------
print("\nPANDAS OPERATIONS")

# Create DataFrame
data = {
    'Name': ['Asha', 'Ravi', 'Kiran'],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:\n", df)

# Operations
print("Average Marks:", df['Marks'].mean())
print("Maximum Marks:", df['Marks'].max())
