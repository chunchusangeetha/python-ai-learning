import pandas as pd

data =[10,23,45,65,76]

series = pd.Series(data)

print(series)

data = {
    "Name": ["Sangeetha", "Rahul", "Anita"],
    "Age": [25, 28, 24],
    "City": ["Hyderabad", "Delhi", "Bangalore"]
}

df = pd.DataFrame(data)
print(df)

print(df.head())# from top
print(df.tail(1))#from last

print(df.shape)

print(df.columns)

print(df.info())

print("names:\n" , df["Name"])

print("names with city:\n",df[["Name","City"]])

df["salary"] = [50000,60000,45000]

print("data with salary:\n",df)

print("avg  age:\n",df["Age"].mean())
print("max  age:\n",df["Age"].max())
print("min  age:\n",df["Age"].min())