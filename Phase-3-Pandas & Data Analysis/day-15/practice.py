import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 
             'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack'],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin', 
             'Mumbai', 'Sydney', 'Toronto', 'Moscow', 'Cairo'],
    'Math': [85, 92, 78, 88, 95, 70, 89, 91, 76, 82],
}

df = pd.DataFrame(data)

#students dataframe

print("students data:\n",df)

# first 2 rows
print("first 2 rows info:\n",df.head(2))

#col names
print("col names:\n",df.columns)

#shape of df
print("shape:",df.shape)


def calculate_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 55: return "C"
    else: return "D"

# Apply the function to the Math column
df['Grade'] = df['Math'].apply(calculate_grade)

print("data with drade col:\n",df)


        