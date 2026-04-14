import pandas as pd 
import numpy as np

customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104, 105],
    "Name": ["John Doe", "Jane Smith", "Alice Brown", None, "Charlie Black"],
    "Email": ["john@email.com", "jane@email.com", "alice@email.com", "bob@email.com", "charlie@email.com"],
    "City": ["New York", "Chicago", "Los Angeles", "Houston", "Miami"]
})
orders = pd.DataFrame({
    "Order_ID": [5001, np.nan, 5003, 5004, 5005],
    "Customer_ID": [101, 102, 101, 103, 105], 
    "Product": ["Laptop", None, "Keyboard", "Monitor", "Webcam"],
    "Quantity": [1, np.nan, 1, 1, 3],
    "Price": [1200, np.nan, 45, 150, 60]
})

merge_left = pd.merge(customers,orders,on="Customer_ID" ,how="left")
print("merged_left:\n", merge_left)


customer_noorder = merge_left[merge_left["Order_ID"].isnull()]
print("customers with no order:\n",customer_noorder)

merge_left["Total"] = merge_left["Quantity"] * merge_left["Price"]
print(merge_left.groupby("Name")["Total"].sum())

print(merge_left.groupby("Name")["Total"].sum().idxmax())

merge_outer = pd.merge(customers, orders, on="Customer_ID", how="outer")

print("OUTER JOIN:\n", merge_outer)