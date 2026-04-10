import pandas as pd 

products_data = {
    'Product_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Product_Name': ['Laptop', 'Smartphone', 'Headphones', 'Monitor', 'Keyboard', 
                     'Mouse', 'Tablet', 'Smartwatch', 'Printer', 'Router'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories', 
                 'Accessories', 'Electronics', 'Accessories', 'Office', 'Networking'],
    'Price': [1200, 800, 150, 300, 50, 25, 450, 200, 250, 100],
    'Stock_Quantity': [15, 30, 50, 20, 100, 150, 25, 40, 10, 60]
}

df = pd.DataFrame(products_data)

print(df)

print(df.info())

products_list_500 = df[df["Price"] < 500]
print("lessthan 500 price productslist:\n",products_list_500)

ele_list = df[df["Category"] == "Electronics"]
print("Ele list:\n", ele_list)

sort_price = df.sort_values(by="Price")
print("sort by price asc:\n",sort_price)

sort_qnt = df.sort_values(by="Stock_Quantity" , ascending=False)
print("sort by sort_qnt:\n",sort_qnt)

print(df.head(2))

print(df.loc[3:6])

print(df.iloc[4:9])

print(df[["Product_Name","Price"]])