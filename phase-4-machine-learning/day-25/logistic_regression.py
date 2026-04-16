import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = {
    "age": [22,25,47,52,46,56,48,55],
    "salary": [20000,25000,50000,60000,52000,65000,48000,70000],
    "bought_insurance": [0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
print(df)

X = df[["age","salary"]]
y= df["bought_insurance"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=42) 

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Actual:", y_test.values)
print("Predicted:", y_pred)

accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")

# Predict new person
new_person = pd.DataFrame([[30,40000]], columns=["age","salary"])
prediction = model.predict(new_person)

print("Will buy insurance?" , "Yes" if prediction[0]==1 else "No")

# task2
person1 = pd.DataFrame([[20,15000]], columns=["age","salary"])
person2 = pd.DataFrame([[60,80000]], columns=["age","salary"])
prediction1 = model.predict(person1)
prediction2 = model.predict(person2)

print(f"{person1} Will buy insurance?" , "Yes" if prediction1[0]==1 else "No")
print(f"{person2} Will buy insurance?" , "Yes" if prediction2[0]==1 else "No")

# task3
print(model.predict_proba(new_person))