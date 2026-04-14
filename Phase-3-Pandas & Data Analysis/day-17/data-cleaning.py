import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Alice"],
    "Age": [25, np.nan, 30, 22, 25],
    "City": ["New York", "London", None, "Tokyo", "New York"],
    "Salary": [50000, 60000, None, 45000, 50000]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

print(df.isnull())

print(df.isnull().sum())

cleaned_df = df.dropna()

print("cleaned df without null null values:\n", cleaned_df)


df["Age"] = df["Age"].fillna(df["Age"].mean())

print("new df",df)

df["Cuty"] = df["City"].fillna("Unknown")

print("new df",df)

df = df.drop_duplicates()

print("After removing duplicates:\n", df)

df.columns = df.columns.str.lower()

print(df.columns)

df["age"] = df["age"].astype(int)
print(df)