import pandas as pd 

data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"],
    "Role": ["Sales", "Marketing", "Sales", "Engineering", "Marketing", "Engineering", "Sales", "Engineering"],
    "Salary": [55000, 48000, 62000, 85000, 51000, 92000, 58000, 88000],
    "Projects": [12, 8, 15, 7, 10, 9, 11, 6]
}

df = pd.DataFrame(data)

print("dataset:\n",df)

grouped = df.groupby("Role")

print(grouped)

print("agg mul",df.groupby("Role")["Salary"].agg(["mean","max","min","count"]))


print("Employees below average salary:\n",df[df["Salary"] < df["Salary"].mean()])

highest_role = df.groupby("Role")["Salary"].mean().idxmax()
print("Highest paying role:", highest_role)

print("no of projects based on role:\n",df.groupby("Role")["Projects"].sum())

idx = df.groupby('Role')['Salary'].idxmax()

result = df.loc[idx, ['Role', 'Employee', 'Salary']]

print("Max salary employee per role:\n", result)

print("Role with higest  avg salary:\n",df.groupby('Role')['Salary'].mean().idxmax())

print("Role with higest  max salary:\n",df.groupby('Role')['Salary'].max().idxmax())
print("Role with higest  min salary:\n",df.groupby('Role')['Salary'].min().idxmax())