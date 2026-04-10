import pandas as pd

data = {
    'Name': ['Aarav', 'Ishani', 'Kabir', 'Meera', 'Arjun', 'Sanya', 'Rohan', 'Ananya', 'Vivaan', 'Diya'],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad', 'Pune', 'Kolkata', 'Ahmedabad', 'Hyderabad', 'Lucknow'],
    'Math': [85, 92, 78, 88, 95, 76, 89, 82, 91, 84],
    'English': [78, 88, 82, 90, 85, 92, 80, 87, 83, 89]
}

df = pd.DataFrame(data)

print("data of students:\n",df)

high = df[df["Math"] > 85]
highinboth_sub = df[(df["Math"] > 85) & (df["English"] > 85)]

print("maths highest marks students:\n",high)
print("Both sub highest marks students:\n",highinboth_sub)

print("Hyd students list:\n",df[df["City"] == "Hyderabad"])

print(df[["Name","Math"]])

print(df.loc[0]) # label base

print(df.loc[2:5, ["Name","Math"]])

print(df.iloc[0:5]) # index base 

sorted_df = df.sort_values(by="English")

print(sorted_df)

sorted_df_math = df.sort_values(by="Math",ascending=False)

print(sorted_df_math)

top_students = df.sort_values(by="Math", ascending=False).head(3)

print(top_students)

df = df.reset_index(drop=True)
print(df)
