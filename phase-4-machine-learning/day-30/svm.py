import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

dataset = load_dataset("aai510-group1/telco-customer-churn")
df = pd.DataFrame(dataset['train'])

df.columns =df.columns.str.strip()

cols_to_drop = [
    'Customer ID ', 'Churn Category', 'Churn Reason',
    'Latitude', 'Longitude', 'Zip Code', 'Churn Score',
    'Customer Status', 'CLTV', 'Total Revenue'
]
df = df.drop(columns=cols_to_drop, errors='ignore')

X = df.drop('Churn',axis = 1)
y = df['Churn']

X_cat_col = X.select_dtypes(include =['object','string']).columns

high_card_cols = [col for col in X_cat_col if X[col].nunique() > 10]

X = X.drop(columns = high_card_cols)

X = pd.get_dummies(X,drop_first = True)

X_train,X_test,y_train,y_test = train_test_split(X,y ,test_size=0.2,random_state = 42)

scaler = StandardScaler();

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: Linear SVM
model_linear = SVC(kernel='linear')

# Model 2: RBF (non-linear)
model_rbf = SVC(kernel='rbf')

# Train
model_linear.fit(X_train_scaled, y_train)
model_rbf.fit(X_train_scaled, y_train)

# Predict
y_pred_linear = model_linear.predict(X_test_scaled)
y_pred_rbf = model_rbf.predict(X_test_scaled)

# Results
print("----- Linear SVM -----")
print("Accuracy:", accuracy_score(y_test, y_pred_linear))
print("Precision:", precision_score(y_test, y_pred_linear))
print("Recall:", recall_score(y_test, y_pred_linear))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_linear))

print("\n----- RBF SVM -----")
print("Accuracy:", accuracy_score(y_test, y_pred_rbf))
print("Precision:", precision_score(y_test, y_pred_rbf))
print("Recall:", recall_score(y_test, y_pred_rbf))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rbf))

model_tuned = SVC(kernel='linear', C=0.5)
model_tuned.fit(X_train_scaled, y_train)

y_pred_tuned = model_tuned.predict(X_test_scaled)

print("Tuned Accuracy:", accuracy_score(y_test, y_pred_tuned))
print("Tuned Recall:", recall_score(y_test, y_pred_tuned))