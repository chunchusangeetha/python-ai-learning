import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix, precision_score, recall_score,classification_report
from sklearn.model_selection import train_test_split

df = pd.read_csv("cat_breed_prediction.csv")

X = df[["weight_kg","tail_length_cm","vocalization_level"]]
y =df["is_persian"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.4,random_state=42) 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

confusion_matrix  = confusion_matrix(y_test, y_pred)
precision_score  = precision_score(y_test, y_pred)
recall_score  = recall_score(y_test, y_pred)
classification_report  = classification_report(y_test, y_pred)

print("accuracy:\n",accuracy)
print("confusion_matrix:\n",confusion_matrix)
print("precision_score:\n",precision_score)
print("recall_score:\n",recall_score)

print(" "*40)
print("classification_report:\n",classification_report)