from datasets import load_dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix

dataset = load_dataset("aai510-group1/telco-customer-churn")
df = pd.DataFrame(dataset['train'])
print(df.head(5))
df.info()

# 1. Remove hidden spaces from column names
df.columns = df.columns.str.strip()

# Drop the noise/leakage/unusefull columns
cols_to_drop = ['Customer ID ','Churn Category', 'Churn Reason', 'Latitude', 'Longitude', 'Zip Code','Churn Score',
    'Customer Status',
    'CLTV',
    'Total Revenue']
df_clean = df.drop(columns=cols_to_drop, errors='ignore')

print(df_clean.head(5))
df_clean.info()

X = df_clean.drop('Churn', axis=1)
y = df_clean['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# This automatically converts all string columns into multiple numeric columns
df_encoded = pd.get_dummies(df_clean)

print(df_encoded.head(5))
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

# Align columns
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

# Model RandomForestClassifier
model = RandomForestClassifier(n_estimators=10, random_state=42)
## model1 DecisionTreeClassifier
model1 = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train
model.fit(X_train, y_train)
# Train DecisionTreeClassifier
model1.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
# Predict DecisionTreeClassifier
y_pred1 = model1.predict(X_test)

# Metrics
print("Accuracy:", accuracy_score(y_test, y_pred),"DecisionTreeClassifier_Accuracy:", accuracy_score(y_test, y_pred1))
print("Precision:", precision_score(y_test, y_pred),"DecisionTreeClassifier_Precision:", precision_score(y_test, y_pred1))
print("Recall:", recall_score(y_test, y_pred),"DecisionTreeClassifier_Recall:", recall_score(y_test, y_pred1))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred),"DecisionTreeClassifier_Confusion Matrix:\n", confusion_matrix(y_test, y_pred1))


print("Feature Importance:", model.feature_importances_)