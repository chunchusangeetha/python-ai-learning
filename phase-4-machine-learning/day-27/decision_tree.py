import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix,recall_score,precision_score

# Load dataset
df = pd.read_csv("cat_breed_prediction.csv")

# Features & target
X = df[["weight_kg","tail_length_cm","vocalization_level"]]
y = df["is_persian"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model
model = DecisionTreeClassifier()


# with LogisticRegression model
model1 = LogisticRegression()

# Train
model.fit(X_train, y_train)
# Train wiith LogisticRegression
model1.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
# predct with LogisticRegression
y_pred1 = model1.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

##Accuracy with LogisticRegression
accuracy1 = accuracy_score(y_test, y_pred1)

print(f"Accuracy: {accuracy:.2f}")

##Accuracy with LogisticRegression
print(f"LogisticRegression Accuracy: {accuracy1:.2f}")

# Confusion Matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
##Confusion Matrix with LogisticRegression
print("LogisticRegression Confusion Matrix:\n", confusion_matrix(y_test, y_pred1))

##Precision  
print("Precision:\n", precision_score(y_test, y_pred))
print("LogisticRegression Precision:\n", precision_score(y_test, y_pred1))

##Recall
print(" Recall:\n", recall_score(y_test, y_pred))
print("LogisticRegression Recall :\n", recall_score(y_test, y_pred1)) 

