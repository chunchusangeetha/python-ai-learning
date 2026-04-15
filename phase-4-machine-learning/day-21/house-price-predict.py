import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house-data.csv")

X = df[["Square_Feet","Bedrooms","Age"]]

y = df[["Price"]]

model = LinearRegression()
#tarin model
model.fit(X,y)

#predict price of new house

test_house = pd.DataFrame([[2000,6,0]], columns=['Square_Feet', 'Bedrooms', 'Age'])
predict_newhouse_price = model.predict(test_house)

print(f"the price of the new house:{predict_newhouse_price[0][0]}")

m = model.coef_[0]   # This is a list of 3 slopes
intercept = model.intercept_[0]

sqft, beds, age = 2000, 6, 0

print(f"Slope (m): {m}")
print(f"Intercept (b): {intercept}")

# The Equation for THIS house:
# Price = (m1 * x1) + (m2 * x2) + (m3 * x3) + intercept
prediction = (m[0]*sqft) + (m[1]*beds) + (m[2]*age) + intercept

print(f"Equation: ({m[0]:.2f} * {sqft}) + ({m[1]:.2f} * {beds}) + ({m[2]:.2f} * {age}) + {y:.2f}")
print(f"Calculated Price: {prediction:,.2f}")