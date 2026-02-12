import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
df = pd.read_csv(r"C:\Users\kathiravan\OneDrive\Desktop\team 15\retail store\retail_store_sales.csv")
print("Before Cleaning:")
print(df.isnull().sum())
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')
df['Price Per Unit'].fillna(df['Price Per Unit'].mean(), inplace=True)
df['Quantity'].fillna(df['Quantity'].median(), inplace=True)
df['Total Spent'].fillna(df['Total Spent'].mean(), inplace=True)
df['Item'].fillna(df['Item'].mode()[0], inplace=True)
df['Discount Applied'].fillna('False', inplace=True)
print("\nAfter Cleaning:")
print(df.isnull().sum())
plt.figure(figsize=(6,4))
plt.boxplot(df['Quantity'])
plt.title("Boxplot for Quantity")
plt.ylabel("Quantity")
plt.show()
z = np.abs(stats.zscore(df['Quantity']))
outliers = df[z > 3]
print("\nOutliers detected:")
print(outliers)