import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

df = pd.read_csv("insurance_data.csv")
X = df[["age","bmi","smoker"]]
y = df["charges"]


X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size = 0.3,random_state=42)

#train model
model = LinearRegression()
model.fit(X_train,y_train)
# test model 
y_pred = model.predict(X_test)
score = r2_score(y_test,y_pred)
#predict chare
print(f"Model Accuracy (R2 Score): {score:2f}")


new_data = pd.DataFrame([[72,35,1]], columns=["age","bmi","smoker"])
print("Predicted charges:", model.predict(new_data)[0])

print(X_train.shape)
print(X_test.shape)

print("Actual:", y_test.values)
print("Predicted:", y_pred)

joblib.dump(model,"insurance_model.pkl")
print("Model saved successfully as insurance_model.pkl")