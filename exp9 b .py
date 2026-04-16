Write a program to implement Matplotlib and Pandas
libraries in python

Aim

To implement and demonstrate the use of Pandas and Matplotlib libraries in Python for data analysis and visualization.
Algorithm
Start the program
Import pandas and matplotlib.pyplot
Create a dataset using Pandas DataFrame
Display the dataset
Plot a graph using Matplotlib
Show the graph
Stop the program

#code
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    'Students': ['Asha', 'Ravi', 'Kiran', 'Neha'],
    'Marks': [85, 90, 78, 88]
}
# Create DataFrame
df = pd.DataFrame(data)
# Display DataFrame
print("DataFrame:\n", df)
# Plot graph
plt.plot(df['Students'], df['Marks'], marker='o')
# Labels and title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks Graph")
# Show graph
plt.show()
