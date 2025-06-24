# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# Display the fir
# st few rows of the dataset
print("First few rows of the Titanic dataset:")
print(titanic.head())

# Data Manipulation: Filtering data (e.g., passengers older than 30)
filtered_data = titanic[titanic['age'] > 30]
print("\nPassengers older than 30:")
print(filtered_data[['age', 'sex', 'class']])

# Data Manipulation: Grouping and Aggregating (average age and fare by class and gender)
grouped_data = titanic.groupby(['class', 'sex']).agg({'age': 'mean', 'fare': 'mean'}).reset_index()
print("\nAverage age and fare by class and gender:")
print(grouped_data)

# Data Visualization: Distribution of passengers' age
plt.figure(figsize=(8, 6))
sns.histplot(titanic['age'], kde=True, bins=30, color='blue')
plt.title('Distribution of Passengers\' Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Data Visualization: Survival rate by class
plt.figure(figsize=(8, 6))
sns.barplot(x='class', y='survived', data=titanic, ci=None, palette='viridis')
plt.title('Survival Rate by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()

# Data Visualization: Survival rate by gender
plt.figure(figsize=(8, 6))
sns.barplot(x='sex', y='survived', data=titanic, ci=None, palette='coolwarm')
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.show()

# Data Manipulation: Adding a new column (e.g., Family Size)
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1
print("\nFirst few rows with the new column 'family_size':")
print(titanic[['survived', 'family_size']].head())

# Data Visualization: Survival rate by family size
plt.figure(figsize=(8, 6))
sns.lineplot(x='family_size', y='survived', data=titanic, ci=None, marker='o')
plt.title('Survival Rate by Family Size')
plt.xlabel('Family Size')
plt.ylabel('Survival Rate')
plt.show()