import pandas as pd

df = pd.read_csv("updated_dataset.csv")
print("Original Dataset:\n", df)
df.info()
print(df.head(3))

print("Employees with salary > 55000:\n",df[df['Salary'] > 55000])

df['Tax'] = df['Salary']*0.05

print("datset with tax col:\n",df)

df.to_csv("final_dataset.csv",index=False)

print("File saved successfully!")