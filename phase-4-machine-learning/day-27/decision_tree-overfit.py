import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix,recall_score,precision_score,f1_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

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
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train
model.fit(X_train, y_train)


# Predict
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)



print(f"Accuracy: {accuracy:.2f}")



# Confusion Matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

##Precision  
print("Precision:\n", precision_score(y_test, y_pred))

##Recall
print(" Recall:\n", recall_score(y_test, y_pred))

#f1_score
print("F1 Score:", f1_score(y_test, y_pred))

plt.figure(figsize=(10,6))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()