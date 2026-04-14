import pandas as pd

employees = pd.DataFrame({
    "Emp_ID": [1,2,3,4],
    "Name": ["Alice","Bob","Charlie","David"],
    "Dept_ID": [101,102,101,103]
})

departments = pd.DataFrame({
    "Dept_ID": [101,102,103,104],
    "Department": ["HR","IT","Finance","Marketing"],
    "Salary": [55000, 48000, 62000, 85000]
})

merged_inner = pd.merge(employees,departments,on="Dept_ID")
print("merged_inner:\n",merged_inner)

merged_left = pd.merge(employees,departments, on="Dept_ID", how="left")
print("merged_left:\n",merged_left)

merged_right = pd.merge(employees,departments, on="Dept_ID", how="right")
print("merged_right:\n",merged_right)

merged_outer = pd.merge(employees,departments, on="Dept_ID", how="outer")
print("merged_outer:\n",merged_outer)

df1 = pd.DataFrame({
    "id": [1,2,3],
    "Name": ["A","B","C"]
})

df2 = pd.DataFrame({
    "emp_id": [1,2,4],
    "Salary": [50000,60000,70000]
})

merged = pd.merge(df1, df2, left_on="id", right_on="emp_id",how="inner")

print(merged)


merged_dataset = df1.set_index("id").join(df2.set_index("emp_id"))
print(merged_dataset)