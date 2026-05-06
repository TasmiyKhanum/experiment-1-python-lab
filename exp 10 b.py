Write a Program to implement various types of
visualization in python.
Aim 
To implement different types of data visualization techniques in Python such as line chart, bar chart, histogram, scatter plot,
box plot, and heatmap using libraries like Matplotlib and Seaborn.
code 
  import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Display first rows
print(df.head())

# 1. Line Chart
plt.figure()
plt.plot(df['column1'], df['column2'])
plt.title("Line Chart")
plt.xlabel("Column1")
plt.ylabel("Column2")
plt.show()

# 2. Bar Chart
plt.figure()
plt.bar(df['column1'], df['column2'])
plt.title("Bar Chart")
plt.xlabel("Column1")
plt.ylabel("Column2")
plt.show()

# 3. Histogram
plt.figure()
plt.hist(df['column1'], bins=10)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.figure()
plt.scatter(df['column1'], df['column2'])
plt.title("Scatter Plot")
plt.xlabel("Column1")
plt.ylabel("Column2")
plt.show()

# 5. Box Plot
plt.figure()
sns.boxplot(data=df)
plt.title("Box Plot")
plt.show()

# 6. Heatmap (Correlation)
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()
