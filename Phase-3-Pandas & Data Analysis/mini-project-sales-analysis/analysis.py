import pandas as pd

df = pd.read_csv("sales.csv")

print('original data set:\n',df)

df.info()
print(df.describe())
# to check null values in daaset 
print(df.isnull().sum())

# fill null values
#cat col with unknown string 
df["Category"] = df["Category"].fillna("Unknown")
#quantity with max val
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
#price with mean
df["Price"]  = df["Price"].fillna(df["Price"].mean())
#cat col with unknown string
df["City"] = df["City"].fillna("Unknown")

print("datset with without null val:\n", df)
df.info()

#remove duplicates in dataset
df = df.drop_duplicates()

# col names to lower case
df.columns = df.columns.str.lower()
#quantity datype float to int
df["quantity"] = df["quantity"].astype(int)
#date dtype
df["order_date"] =  pd.to_datetime(df['order_date'])
#cleaned data
print("cleaned dataset:\n", df)

#new col revenue
df["revenue"] = df["quantity"]*df["price"]
print("df...:\n",df)

#most revenue earns product
product_earns_most = df.groupby("product")["revenue"].sum().idxmax()
print(f"Top revenue generating product: {product_earns_most}")

#least revenue earns product
product_earns_least = df.groupby("product")["revenue"].sum().idxmin()
print(f"low revenue generating product: {product_earns_least}")

city_generates_highest = df.groupby("city")["revenue"].sum().idxmax()
print(f"Top revenue generating city: {city_generates_highest}")

based_on_quantity = df.groupby("product")["quantity"].sum().idxmax()
top_quantity_value = df.groupby("product")["quantity"].sum().max()
print(f"Top selling product (by quantity): {based_on_quantity }  ({top_quantity_value})")

monthly_trend = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum()
print("Monthly Sales Trend:\n", monthly_trend)

category_performance = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
print("Category Performance:\n", category_performance)

best_category = category_performance.idxmax()
print(f"\nThe best performing category is: {best_category}")

df.to_csv("updatedsales.csv",index=False)
print("File saved successfully!")