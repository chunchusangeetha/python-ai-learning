import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score 
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("house-data.csv")

X = df[["Square_Feet","Bedrooms","Age"]]
y = df["Price"]

X_train,X_test,y_train,y_test = train_test_split(X,y ,test_size = 0.2 ,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

score = r2_score(y_test,y_pred)

print(f"Model Accuracy (R2 Score): {score:2f}")

print(model.predict([[1660, 4, 6]]))

#  saves 'model' object into a file called 'house_model.pkl'
joblib.dump(model, 'house_model.pkl')
print("Model saved successfully as house_model.pkl")