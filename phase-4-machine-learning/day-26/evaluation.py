import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix, precision_score, recall_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = {
    "age": [22, 25, 47, 52, 46, 56, 48, 55, 56, 46, 32, 60, 25, 38, 56, 36, 40, 28, 28, 41, 53, 57, 41, 20, 39, 19, 41, 61, 47, 55, 19, 38, 50, 29, 39, 61, 42, 44, 59, 45, 33, 32, 64, 61, 20, 54, 24, 38, 26, 56, 35, 21, 42, 31, 26, 43, 19, 37, 45, 64],
    "salary": [20000, 25000, 50000, 60000, 52000, 65000, 48000, 70000, 67699, 58270, 32575, 73626, 26552, 40585, 64543, 44155, 44473, 28021, 30843, 50589, 66692, 68673, 48275, 17561, 44497, 17195, 50229, 76067, 50816, 67269, 22639, 46892, 60263, 36116, 48729, 67478, 53068, 51087, 69059, 53731, 41571, 40484, 77408, 71876, 19462, 58264, 30206, 41568, 30063, 62627, 38095, 28287, 49058, 36218, 31336, 45391, 22092, 41361, 53584, 73299],
    "bought_insurance": [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1]
}


df = pd.DataFrame(data)
print(df)

X = df[["age","salary"]]
y= df["bought_insurance"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state=42) 

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


## Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

## recision_score
precision = precision_score(y_test, y_pred)
print(f"Precision: {precision:.2f}")

## recall
recall = recall_score(y_test, y_pred)
print(f"Recall: {recall:.2f}")

## classification_report
print("classification_report:\n",classification_report(y_test, y_pred))