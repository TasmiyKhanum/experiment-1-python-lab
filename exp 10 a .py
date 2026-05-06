Write Program to Load, Clean and Exploring the data using python.
aim : To load a dataset, clean the data by handling missing values
and duplicates, and perform basic exploratory data analysis (EDA) using Python in order to understand the structure, patterns, 
and relationships in the data.

#code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 2. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numeric values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nData cleaned successfully!")

# 3. Data Exploration
print("\nUnique values in each column:")
print(df.nunique())

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# 4. Visualization
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

# Example scatter plot (change column names as needed)
# plt.scatter(df['column1'], df['column2'])
# plt.xlabel('column1')
# plt.ylabel('column2')
# plt.show()

# 5. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved as 'cleaned_data.csv'")
