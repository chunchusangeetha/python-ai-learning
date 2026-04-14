import pandas as pd

df = pd.read_csv("dataset.csv")

df.info()

print(df.head())
print(df.describe())

high_salary = df[df["Salary"] > 60000]
print("High salary:\n", high_salary)

df["Bonus"] = df["Salary"] * 0.10
print(df)

df.to_csv("updated_dataset.csv", index=False)
