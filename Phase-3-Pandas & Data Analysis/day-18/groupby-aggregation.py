import pandas as pd

data = {
    "Name": ["A","B","C","D","E","F","G"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance"],
    "Salary": [60000,50000,70000,65000,52000,72000,68000],
    "Experience": [2,3,5,4,2,6,5]
}

df = pd.DataFrame(data)

print("dataset:\n",df)

grouped = df.groupby("Department")

print(grouped)

print("mean:\n",df.groupby("Department")["Salary"].mean())
print("max:\n",df.groupby("Department")["Salary"].max())
print("min:\n",df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Name"].count())

print("mult agg:\n",df.groupby("Department")["Salary"].agg(["mean","max","min"]))

print(df.groupby("Department")[["Salary","Experience"]].mean())

result = df.groupby("Department")["Salary"].mean().reset_index()

print("result:\n",result)

result = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)

print(result)

highest = df.groupby("Department")["Salary"].mean().idxmax()

print("Highest paying department:", highest)