import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G","C"],
    "Age": [25, np.nan, 30, 22, np.nan, 35, 28,30],
    "City": ["Delhi", "Mumbai", None, "Tokyo", "London", "New York", None,None],
    "Salary": [50000, 60000, 55000, np.nan, 45000, 80000, 62000,55000]
}

df = pd.DataFrame(data)

print("Original Dataset:\n",df)

print(df.isnull())

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("update df:\n", df)
df.info()

# remove duplicate
df = df.drop_duplicates()

df.columns = df.columns.str.lower()

# age to int
df["age"] = df["age"].astype(int)

print("Final cleaned dataset:\n",df)
